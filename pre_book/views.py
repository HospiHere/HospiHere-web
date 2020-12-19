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

def pre_book(request):
    user = request.user.username
    doc_ref = db.collection(u'booking').where(u'hospital', u'==', user).stream()
    items=[]
    for doc in doc_ref:
        items.append(doc.to_dict())
        
    return render(request,"pre_book.html", {'content': items})

def update(request, disease, hospital, mobile, preBook_date):
    patient_name = request.POST.get('patient_name')
    patient_address = request.POST.get('patient_address')
    bed_type = request.POST.get('bed_type')

    db.collection(u'booking').document(disease + hospital + mobile + preBook_date).update({
    "status": "Confirm",
    "disease_check": disease,
    "patient_name": patient_name,
    "patient_address": patient_address,
    "bedType" : bed_type,
    })

    db.collection(u'hospitals').document(hospital).update({
    "booked" : {bed_type: Increment(1)},
    "bed" : {bed_type: Increment(-1)},
    })

    user = request.user.username
    doc_ref = db.collection(u'booking').where(u'hospital', u'==', user).stream()
    items=[]
    for doc in doc_ref:
        items.append(doc.to_dict())

    return render(request,"pre_book.html", {'content': items})

    