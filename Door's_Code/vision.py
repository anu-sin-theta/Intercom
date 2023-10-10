# import cv2
# import time
# import smtplib
# from email.message import EmailMessage
#
# # Function to send an email notification
# def send_email():
#     gmail_user = "atcsedintercom@gmail.com"
#     gmail_pwd = "kucu kfwv cspf vmph"
#     receiver = ['audiq4456@gmail.com']  # must be a list
#
#     try:
#
#         mail_content = EmailMessage()
#
#         # Mail metadata
#         mail_content['Subject'] = "Activity Detected at the Staff Door"
#         mail_content['From'] = gmail_user
#         mail_content['To'] = receiver
#
#         # Prepare HTMl Formatted Mail
#         mail_content.set_content('''<!DOCTYPE html>
#         <html>
# <head>
#     <style>
#         body {
#             background-color: #2196F3;
#             font-family: Arial, sans-serif;
#             text-align: center;
#             background: linear-gradient(to bottom, purple, #2196F3);
#             background-size: cover;
#             background-repeat: no-repeat;
#             background-attachment: fixed;
#             height: 100vh;
#             margin: 0;
#             display: flex;
#             flex-direction: column;
#             justify-content: center;
#             align-items: center;
#         }
#
#         h1 {
#             color: #333333;
#             padding-top: 40px;
#             font-size: 50px;
#         }
#
#         .card {
#             background-color: white;
#             width: 300px;
#             border-radius: 10px;
#             padding: 20px;
#             box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
#         }
#
#         .button {
#             background-color: #2196F3;
#             color: white;
#             padding: 10px 20px;
#             border: none;
#             border-radius: 5px;
#             text-decoration: none;
#             margin-top: 20px;
#             display: inline-block;
#             font-size: 16px;
#         }
#
#         .button:hover {
#             background-color: #1976D2;
#         }
#     </style>
# </head>
# <body>
#     <h1>INTERCOM at CSED</h1>
#
#     <div class="card">
#         <h2>Message</h2>
#         <p>This is Intercom systems, please check the doors activity </p>
#     </div>
#
#     <a class="button" href="csedintercom.pages.dev">The Intercom</a>
#
#     <div class="card">
#         <h3>At Staff door.</h3>
#         <p>SECURE V 1.0.</p>
#     </div>
# </body>
# </html>''', subtype='html')
#
#         # Add attachments as well
#         with open("./face_detected.jpg", "rb") as attachment:
#             mail_content.add_attachment(attachment.read(), maintype="application", subtype="octet-stream",
#                                         filename=attachment.name)
#
#         with smtplib.SMTP_SSL('smtp.gmail.com') as mail_account:
#             mail_account.login(user=gmail_user, password=gmail_pwd)
#             mail_account.send_message(mail_content)
#     except Exception as e:
#         print("Error sending email:", e)
#
#
# # Initialize variables
# start_time = None
# face_detected = False
# mail_sent = False
#
# # Initialize the webcam and face cascade classifier
# cap = cv2.VideoCapture(0)
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#
# while True:
#     # Read a frame from the webcam
#     ret, frame = cap.read()
#
#     if not ret:
#         break
#
#     # Convert the frame to grayscale for face detection
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Detect faces in the frame
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#
#     # Process detected faces
#     if len(faces) > 0:
#         if not face_detected:
#             start_time = time.time()
#             face_detected = True
#
#         elapsed_time = time.time() - start_time
#         cv2.imwrite('./face_detected.jpg', frame)
#
#         # Check if faces are still detected after 6 seconds
#         if elapsed_time > 6:
#             print("Faces still detected after 6 seconds")
#             if not mail_sent:
#                 send_email()
#                 mail_sent = True
#
#     else:
#         face_detected = False
#         mail_sent = False
#
#     # Pause for 10 seconds after sending mail
#     if mail_sent and elapsed_time > 16:
#         mail_sent = False
#
#     # Display the frame
#     cv2.imshow('Face Detection', frame)
#
#     # Exit the loop if the 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Release the webcam and close the OpenCV window when the program exits
# cap.release()
# cv2.destroyAllWindows()

import cv2
import os
import time

image_dir = "captured_images"

if not os.path.exists(image_dir):
    os.makedirs(image_dir)

while True:
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        break

    ret, frame = cap.read()

    if ret:
        timestamp = int(time.time())
        image_filename = os.path.join(image_dir, f"{timestamp}.jpg")
        cv2.imwrite(image_filename, frame)
        cap.release()

        print(f"Image captured and saved as {image_filename}")
        time.sleep(5)

        current_time = time.time()
        for filename in os.listdir(image_dir):
            file_timestamp = int(filename.split(".")[0])
            if current_time - file_timestamp > 60:
                file_path = os.path.join(image_dir, filename)
                os.remove(file_path)
                print(f"Removed image: {file_path}")

    # Release the camera
    cap.release()
