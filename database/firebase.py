import pyrebase
import json
import firebase_admin
from firebase_admin import credentials
import os
from dotenv import load_dotenv

load_dotenv()

config= {
    "FIREBASE_SERVICE_ACCOUNT_KEY" :     os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY"),
    "FIREBASE_CONFIG" : os.getenv('FIREBASE_CONFIG')
              
}
# Initialize Firebase Admin with the service account information
cred = credentials.Certificate(json.loads(config['FIREBASE_SERVICE_ACCOUNT_KEY']))
firebase_admin.initialize_app(cred)
# load firebase config
firebase = pyrebase.initialize_app(json.loads(config['FIREBASE_CONFIG']))
# init firebase as db
db = firebase.database()
# init firebase as authSession
authSession = firebase.auth()