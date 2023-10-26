import cv2
import face_recognition
import os
import time

def face_camera(known_faces, known_names):
    cap = cv2.VideoCapture(0)
    image_dir = "captured_images"

    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Face recognition
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_faces, face_encoding)

            name = "Unknown"

            if True in matches:
                matched_index = matches.index(True)
                name = known_names[matched_index]
            top, right, bottom, left = face_locations[0]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        # Capture and save images
        # timestamp = int(time.time())
        # image_filename = os.path.join(image_dir, f"{timestamp}.jpg")
        # cv2.imwrite(image_filename, frame)
        #
        # print(f"Image captured and saved as {image_filename}")

        current_time = time.time()
        for filename in os.listdir(image_dir):
            file_timestamp = int(filename.split(".")[0])
            if current_time - file_timestamp > 60:
                file_path = os.path.join(image_dir, filename)
                os.remove(file_path)
                print(f"Removed image: {file_path}")

        cv2.imshow('Recognized Faces', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

known_face_images = [
    face_recognition.load_image_file("recognized/n.jpg"), face_recognition.load_image_file("recognized/a.jpg"),face_recognition.load_image_file("recognized/aryan.jpeg")
]

known_face_encodings = [face_recognition.face_encodings(image)[0] for image in known_face_images]
print(known_face_encodings)

known_faces = known_face_encodings
known_names = ["Nandini", "Anubhav","Rad Monk"]

face_camera(known_faces, known_names)
