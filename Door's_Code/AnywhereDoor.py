import time
import smtplib
from email.message import EmailMessage
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os
cred = credentials.Certificate("csed-intercom-firebase-adminsdk-m46ay-86ce3b9853.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://csed-intercom.asia-southeast1.firebasedatabase.app/'
})

ref1 = db.reference('allowButton')
ref2 = db.reference('denyButton')
ref3 = db.reference('viewButton')
ref4 = db.reference('doorStatus')
ref5 = db.reference('cameraStatus')


# def servo(angle):
#
#     GPIO.setmode(GPIO.BOARD)
#
#     servo_pin = 12
#
#     frequency = 50
#
#     duty_cycle_min = 2.5
#     duty_cycle_max = 12.5
#
#     angle = 180
#
#     duty_cycle = (duty_cycle_max - duty_cycle_min) * angle / 180.0 + duty_cycle_min
#     servo_pwm = None
#     try:
#         GPIO.setup(servo_pin, GPIO.OUT)
#         servo_pwm = GPIO.PWM(servo_pin, frequency)
#         servo_pwm.start(duty_cycle_min)
#
#         servo_pwm.ChangeDutyCycle(duty_cycle)
#         time.sleep(1)  # Wait for the servo to reach the desired position
#
#         # Clean up
#         servo_pwm.stop()
#         GPIO.cleanup()
#     except KeyboardInterrupt:
#         servo_pwm.stop()
#         GPIO.cleanup()
#         return "Open"


# def opendoor():
#     # servo(0)
#
#
# def closedoor():
#     # servo(180)


def send_email():
    gmail_user = "atcsedintercom@gmail.com"
    gmail_pwd = "kucu kfwv cspf vmph"
    receiver = ['tiwariojas578@gmail.com']  # must be a list

    mail_content = EmailMessage()

    # Mail metadata
    mail_content['Subject'] = "Activity at the Staff Door"
    mail_content['From'] = gmail_user
    mail_content['To'] = receiver

    mail_content.set_content('''<!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                background-color: #2196F3;
                font-family: Arial, sans-serif;
                text-align: center;
                background: linear-gradient(to bottom, purple, #2196F3);
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
                height: 100vh;
                margin: 0;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }

            h1 {
                color: #333333;
                padding-top: 40px;
                font-size: 50px;
            }

            .card {
                background-color: purple;
                width: 300px;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
            }

            .button {
                background-color: #2196F3;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                text-decoration: none;
                margin-top: 20px;
                display: inline-block;
                font-size: 16px;
            }

            .button:hover {
                background-color: #1976D2;
            }
        </style>
    </head>
    <body>
        <h1>Intercom at CSED</h1>

        <div class="card">
            <h2>Message</h2>
            <p>This is Intercom systems, please check the door's activity. </p>
        </div>

        <a class="button" href="intercomcsed.pages.dev/intercom">The Intercom</a>

        <div class="card">
            <h3>At Staff door.</h3>
            <p>Developed at research wing by Anubhav Singh.</p>
        </div>
    </body>
    </html>''', subtype='html')

    image_dir = "captured_images"
    latest_image = max([os.path.join(image_dir, f) for f in os.listdir(image_dir)], key=os.path.getctime)

    with open(latest_image, "rb") as attachment:
        mail_content.add_attachment(attachment.read(), maintype="application", subtype="octet-stream",
                                    filename=latest_image)

    # Send the email
    with smtplib.SMTP_SSL('smtp.gmail.com') as mail_account:
        mail_account.login(user=gmail_user, password=gmail_pwd)
        mail_account.send_message(mail_content)



while True:
        try:
            data1 = ref1.get()
            data2 = ref2.get()
            data3 = ref3.get()
            print(data1)
            print(data2)
            print(data3)
            time.sleep(1)

            doorStatus = "Open"
            if doorStatus == "Open":
                ref4.set("Open")
            else:
                ref4.set("Close")

            if data3 == "View":
                send_email()
                time.sleep(2)
            else:
                pass
            if data1 == "Allow":
                pass
            else:
                pass

            if data2 == "Deny":
                # closedoor()
                pass


        except Exception as e:
            print("Error retrieving data:", e)


