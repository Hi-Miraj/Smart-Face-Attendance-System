# **Smart Facial Recognition Attendance System**

This project utilizes advanced facial recognition technologies to develop a smart attendance system that integrates with Firebase for real-time data updates and also logs attendance data in an Excel file for further analysis. The system is powered by `dlib` with more than 96% accuracy, according to studies from Oxford University, and recognizes faces based on various key facial features. The project also integrates with an Arduino system for real-time interaction and feedback.

## **Key Features**

- **Real-Time Face Recognition:** Utilizes `face_recognition` library to detect and recognize faces in real-time using a webcam.
- **Firebase Integration:** The system logs attendance data to Firebase Realtime Database for remote tracking and monitoring.
- **Excel Logging:** Data is also logged locally in an Excel file for deeper analysis.
- **Arduino Integration:** The system sends real-time signals to an Arduino board to perform actions such as triggering LEDs or other components based on attendance recognition.
- **High Accuracy with dlib:** The face detection process uses `dlib`, which analyzes different areas of the face (eyes, nose, jawline, etc.) to ensure robust detection accuracy, exceeding 96% based on Oxford University's tests.

---

## **Technical Overview**

The system is built around two primary components: 

1. **Facial Recognition System**  
   - **Libraries Used:**
     - `face_recognition`: For detecting and encoding faces.
     - `dlib`: For achieving highly accurate face detection using landmarks and key facial areas.
     - `OpenCV`: For camera interface and image processing.
     - `firebase_admin`: For real-time data syncing with Firebase Realtime Database.
     - `serial`: For communication with Arduino hardware.

   - **How dlib Works for Face Detection:**
     The system leverages `dlib`'s facial landmarks detection, which analyzes the geometric layout of the face. The face is broken down into key regions such as the eyes, nose, and jaw, and the relative distances and angles of these features are used to uniquely identify individuals. This method is highly resistant to changes in lighting and angle, ensuring a more reliable recognition system.

2. **Kivy-based GUI for Face Recognition:**
   - **Libraries Used:**
     - `Kivy`: For building a graphical user interface (GUI) to trigger and display face recognition results.
     - `threading`: To run facial recognition in the background without blocking the UI thread.
     - `requests`: For sending the recognized name to a web server or backend.

   - **Face Recognition Flow in the GUI:**
     The GUI allows users to start the facial recognition process by pressing a button. Once initiated, the system captures images from the webcam, detects faces, and compares them to a database of known faces. When a match is found, the name is displayed on the GUI and sent to a server for further action.

---

## **Technologies Used**

- **Python Libraries:**
  - `opencv-python`: For real-time computer vision tasks.
  - `face_recognition`: For facial feature extraction and comparison.
  - `numpy`: For handling arrays and matrix operations.
  - `firebase-admin`: For interacting with Firebase services.
  - `dlib`: For facial landmark detection with high accuracy.
  - `Kivy`: For building the interactive GUI.
  - `requests`: For sending data to a server.
  - `serial`: For communication with Arduino hardware.

- **Hardware Used:**
  - **Webcam**: For capturing real-time video feeds.
  - **Arduino**: For receiving signals based on detected face matches and performing actions (e.g., activating LEDs).
  - **Raspberry Pi (optional)**: Can be used as a base station for running the system in an embedded environment.

---

## **How the System Works**

### **Face Detection and Recognition**
1. The system loads known face images stored in the `images` directory.
2. Faces are detected and encoded using the `face_recognition` library.
3. When a face is detected via webcam, its encoding is compared to the known face encodings.
4. If a match is found, the person's name is displayed, and the attendance is logged into Firebase Realtime Database.
5. If a specific "guilty" individual (e.g., someone with a disease like Dengue) is detected, a special signal (`'T'`) is sent to Arduino for further actions, otherwise a regular signal (`'O'`) is sent.
6. For unrecognized faces, the system assigns a unique ID and logs their attendance in Firebase.

### **GUI for Face Recognition**
1. The GUI allows the user to start the facial recognition process via a button.
2. It runs the face recognition in a separate thread to avoid freezing the user interface.
3. The result is displayed in the GUI, and the recognized name is sent to the server for further processing.

---

## **How to Run**

### **Setup the Environment:**

1. **Clone this repository:**

```bash
git clone https://github.com/yourusername/smart-facial-recognition-attendance.git
cd smart-facial-recognition-attendance
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should include all the libraries you need, such as:
- opencv-python
- face_recognition
- firebase-admin
- numpy
- dlib
- kivy
- requests

3. **Firebase Configuration:**
   - Set up a Firebase project and create a service account key.
   - Replace `'face-detection-31d91-firebase-adminsdk-89zyu-2ab2461b00.json'` with the path to your Firebase service account key JSON file.

4. **Arduino Configuration:**
   - Connect an Arduino board to your computer and set the correct COM port in the script (e.g., `'COM4'`).
   - Upload the corresponding Arduino code to handle serial communication.

5. **Start the Kivy App:**
   - Run the Kivy app by executing:

```bash
python facial_recognition_gui.py
```

This will launch the GUI for starting face recognition.

6. **Start the Face Recognition System:**
   - The system will use your webcam to detect and recognize faces in real-time.
   - The recognized name will be sent to Firebase and displayed in the GUI.

---

## **Contributing**

We welcome contributions! Feel free to open issues or submit pull requests. Ensure you follow the coding standards and provide detailed descriptions of your changes.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### **Acknowledgments**
- Special thanks to [Oxford University](https://www.ox.ac.uk) for their research on facial recognition accuracy.
- This project leverages cutting-edge technologies in computer vision and real-time databases.

---





