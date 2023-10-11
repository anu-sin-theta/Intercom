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

def check_door():
    return "Open"

def opendoor():
    return "Door Opened"

def closedoor():
    return "Door Closed"



def send_email():
    gmail_user = "atcsedintercom@gmail.com"
    gmail_pwd = "kucu kfwv cspf vmph"
    receiver = ['shekharupadhyay7983@gmail.com']  # must be a list

    mail_content = EmailMessage()

    # Mail metadata
    mail_content['Subject'] = "Activity Detected at the Staff Door"
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

        <a class="button" href="csedintercom.pages.dev">The Intercom</a>

        <div class="card">
            <h3>At Staff door.</h3>
            <p>Developed at research wing by Anubhav singh.</p>
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

            doorStatus = check_door()
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
                opendoor()
            else:
                closedoor()
            if data2 == "Deny":
                closedoor()



        except Exception as e:
            print("Error retrieving data:", e)


