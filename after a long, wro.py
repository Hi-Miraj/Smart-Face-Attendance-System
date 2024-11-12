import face_recognition
import cv2
import requests
import os
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

class FacialRecognitionApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Button to start face recognition
        self.start_button = Button(text="Start Facial Recognition")
        self.start_button.bind(on_press=self.start_face_recognition)
        self.layout.add_widget(self.start_button)

        # Label to show the result
        self.result_label = Label(text="Face recognition results will be shown here.")
        self.layout.add_widget(self.result_label)

        return self.layout

    def start_face_recognition(self, instance):
        # Run face recognition in a separate thread
        thread = threading.Thread(target=self.recognize_face)
        thread.start()

    def recognize_face(self):
        # Load known faces and their encodings
        known_face_encodings = []
        known_face_names = []

        images_dir = 'images'
        for image_name in os.listdir(images_dir):
            image_path = os.path.join(images_dir, image_name)
            known_face = face_recognition.load_image_file(image_path)
            face_encoding = face_recognition.face_encodings(known_face)[0]
            known_face_encodings.append(face_encoding)
            known_face_names.append(os.path.splitext(image_name)[0])

        # Open webcam
        video_capture = cv2.VideoCapture(0)
        recognized_name = "Unknown"

        start_time = cv2.getTickCount()
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            rgb_frame = frame[:, :, ::-1]
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                if True in matches:
                    first_match_index = matches.index(True)
                    recognized_name = known_face_names[first_match_index]
                    break

            # Draw boxes around recognized faces
            for (top, right, bottom, left) in face_locations:
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                # Put name below the box
                cv2.putText(frame, recognized_name, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            # Display the frame with the camera preview
            cv2.imshow('Camera Preview', frame)

            # Exit after 5 seconds
            elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
            if elapsed_time > 5:
                break

            # Allow a brief delay to ensure the display refreshes
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the webcam and close the camera preview window
        video_capture.release()
        cv2.destroyAllWindows()

        # Send recognized name to the server
        if recognized_name != "Unknown":
            self.send_name_to_server(recognized_name)

    def send_name_to_server(self, name):
        url = 'http://localhost:5000/submit_name'  # Use the correct URL for the Flask server
        try:
            response = requests.post(url, json={'name': name})
            if response.status_code == 200:
                self.update_result(f"Name sent to website: {name}")
            else:
                self.update_result("Failed to send name.")
        except Exception as e:
            self.update_result(f"Error: {str(e)}")

    def update_result(self, message):
        # Update the result label with the given message
        def update_text(dt):
            self.result_label.text = message

        Clock.schedule_once(update_text)

if __name__ == '__main__':
    FacialRecognitionApp().run()
