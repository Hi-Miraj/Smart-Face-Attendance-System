import cv2
import face_recognition


img1 = face_recognition.load_image_file('obama.jpg')
img1= cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img1test = face_recognition.load_image_file('obama_partial_face.jpg')
img1test = cv2.cvtColor(img1test, cv2.COLOR_BGR2RGB)

face = face_recognition.face_locations(img1)[0]
#print(face)
encodeFace = face_recognition.face_encodings(img1)[0]
print(encodeFace)
cv2.rectangle(img1, (face[3],face[0]),(face[1],face[2]), (0,255,0), 3)

faceTest = face_recognition.face_locations(img1test)[0]
encodetestFace = face_recognition.face_encodings(img1test)[0]
cv2.rectangle(img1test, (face[3],face[0]),(face[1],face[2]), (0,255,0), 3)

res = face_recognition.compare_faces([encodeFace],encodetestFace)
face_Dis = face_recognition.face_distance([encodeFace],encodetestFace)
print(res, face_Dis)

cv2.putText(img1test, f"{res} {round(face_Dis[0], 2)}", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
cv2.imshow('Obama', img1)
cv2.imshow('Obama Test', img1test)
cv2.waitKey()
cv2.destroyAllWindows()