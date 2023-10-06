import time
import cv2
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import threading

cred = credentials.Certificate("csed-intercom-firebase-adminsdk-m46ay-86ce3b9853.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://csed-intercom.asia-southeast1.firebasedatabase.app/'
})
# printing all the data1 in the database for testing

ref1 = db.reference('allowButton')
ref2 = db.reference('denyButton')
ref3 = db.reference('viewButton')
ref4 = db.reference('doorStatus')
ref5 = db.reference('camera')


def door():
    return "Open"


def transmit_camera():
    print("Transmitting camera")


while 1:
    try:
        time.sleep(1)
        data1 = ref1.get()
        data2 = ref2.get()
        data3 = ref3.get()
        if data3 == "View":
            t1 = threading.Thread(target=transmit_camera)
            t1.start()
        print("Data retrieved from the database:", data1)
        print("Data retrieved from the database:", data2)
        print("Data retrieved from the database:", data3)
        doorStatus = door()
        if doorStatus == "Open":
            ref4.set("Open")
        else:
            ref4.set("Close")

    except Exception as e:
        print("Error retrieving data1:", e)
