from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1 import Increment

# Create your views here.
db = firestore.client()

def testBooking(request):
    user = request.user.username
    doc_ref = db.collection(u'testBooking').where(u'hospital', u'==', user).stream()
    items=[]
    for doc in doc_ref:
        items.append(doc.to_dict())
        
    return render(request,"testBooking.html", {'content': items})

def update(request, testName, hospital, mobile, testAppointmentDate, testAppointmentTime):
    patient_name = request.POST.get('patient_name')
    patient_address = request.POST.get('patient_address')
    appointmentTime = request.POST.get('testAppointmentTime')

    db.collection(u'testBooking').document(testName + hospital + mobile + testAppointmentDate + testAppointmentTime).update({
    "status": "Confirm",
    "patient_name": patient_name,
    "patient_address": patient_address,
    "testAppointmentTime": appointmentTime,
    })

    user = request.user.username
    doc_ref = db.collection(u'testBooking').where(u'hospital', u'==', user).stream()
    items=[]
    for doc in doc_ref:
        items.append(doc.to_dict())

    return render(request,"testBooking.html", {'content': items})

    