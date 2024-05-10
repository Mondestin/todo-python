import pyrebase
import json
import firebase_admin
from firebase_admin import credentials
from dotenv import dotenv_values
from dotenv import load_dotenv
import os
# get variables from .env file
config = dotenv_values(".env")

# load_dotenv()

# config= {
#     "FIREBASE_SERVICE_ACCOUNT_KEY" :     os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY"),
#     "FIREBASE_CONFIG" : os.getenv('FIREBASE_CONFIG')         
# }
firebase_config  =  json.loads(config['FIREBASE_CONFIG'])
firebase_service_account_key = json.loads(config["FIREBASE_SERVICE_ACCOUNT_KEY"])

# Initialize Firebase Admin with the service account information
cred = credentials.Certificate(firebase_service_account_key)
firebase_admin.initialize_app(cred)
# load firebase config
firebase = pyrebase.initialize_app(firebase_config)
# init firebase as db
db = firebase.database()
# init firebase as authSession
authSession = firebase.auth()