import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate('/Users/hat/Documents/GitHub/get_syllabus_info_from_web_site/get-syllabus-info-43b21-firebase-adminsdk-jogd9-97e9407f2d.json')
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

# CSV file path
csv_path = '/Users/hat/Documents/GitHub/get_syllabus_info_from_web_site/syllabus_data.csv'

# Read CSV file
df = pd.read_csv(csv_path, header=None, names=[
    'course_name', 'course_objective', 'course_plan', 'course_period',
    'grade_allocation', 'credits', 'required_elective', 'instructor', 'educational_program'
])

# Convert DataFrame to a list of dictionaries
data = df.to_dict(orient='records')

# Write data to Firestore
for item in data:
    doc_ref = db.collection('syllabus').document()
    doc_ref.set(item)

print("Data has been successfully written to Firestore.")