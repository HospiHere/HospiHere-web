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

def hospiProfile(request):
    user = request.user.username
    doc_ref = db.collection(u'hospitals').where(u'name', u'==', user).stream()
    items=[]
    for doc in doc_ref:
        items.append(doc.to_dict())
        
    return render(request,"hospiProfile.html", {'content': items})

def branch(request):
    user = request.user.username
    branch = request.POST.get('branch')

    db.collection(u'hospitals').document(user).update({
        "branch" : branch,
        })

    doc_ref = db.collection(u'hospitals').where(u'name', u'==', user).stream()
    items=[]
    for doc in doc_ref:
        items.append(doc.to_dict())
        
    return render(request,"hospiProfile.html", {'content': items})

def email(request):
    user = request.user.username
    email = request.POST.get('email')

    db.collection(u'hospitals').document(user).update({
        "email" : email,
        })

    doc_ref = db.collection(u'hospitals').where(u'name', u'==', user).stream()
    items=[]
    for doc in doc_ref:
        items.append(doc.to_dict())
        
    return render(request,"hospiProfile.html", {'content': items})

def latitude(request):
    user = request.user.username
    latitude = request.POST.get('latitude')

    #db.collection(u'hospitals').document(user).update({
    #    "location" : {
    #        "latitude" : latitude,
    #    }
    #    })

    doc_ref = db.collection(u'hospitals').where(u'name', u'==', user).stream()
    items=[]
    for doc in doc_ref:
        items.append(doc.to_dict())
        
    return render(request,"hospiProfile.html", {'content': items})

def bed(request):
    user = request.user.username
    icu = request.POST.get('icu')
    emergency = request.POST.get('emergency')
    ward = request.POST.get('ward')

    db.collection(u'hospitals').document(user).update({
        "bed" : {
                        "emergency" : int(emergency),
                        "icu" : int(icu),
                        "ward": int(ward),
                    },
        })

    doc_ref = db.collection(u'hospitals').where(u'name', u'==', user).stream()
    items=[]
    for doc in doc_ref:
        items.append(doc.to_dict())
        
    return render(request,"hospiProfile.html", {'content': items})

def test(request):
    user = request.user.username
    test = request.POST.getlist('DynamicTextBox')

    test_ref = db.collection(u'hospitals').document(user)
    test_ref.update({u'availableTest': firestore.ArrayUnion(test)})

    doc_ref = db.collection(u'hospitals').where(u'name', u'==', user).stream()
    items=[]
    for doc in doc_ref:
        items.append(doc.to_dict())
        
    return render(request,"hospiProfile.html", {'content': items})

def remove(request, test):
    user = request.user.username

    test_ref = db.collection(u'hospitals').document(user)
    test_ref.update({u'availableTest': firestore.ArrayRemove([test])})

    doc_ref = db.collection(u'hospitals').where(u'name', u'==', user).stream()
    items=[]
    for doc in doc_ref:
        items.append(doc.to_dict())
        
    return render(request,"hospiProfile.html", {'content': items})

def specialized(request):
    user = request.user.username
    diseaseSpecialized = request.POST.getlist('DynamicSpecialistBox')

    specialization = db.collection(u'hospitals').document(user)
    specialization.update({u'specialization': firestore.ArrayUnion(diseaseSpecialized)})

    doc_ref = db.collection(u'hospitals').where(u'name', u'==', user).stream()
    items=[]
    for doc in doc_ref:
        items.append(doc.to_dict())
        
    return render(request,"hospiProfile.html", {'content': items})

def removeSp(request, specialized):
    user = request.user.username

    specialization = db.collection(u'hospitals').document(user)
    specialization.update({u'specialization': firestore.ArrayRemove([specialized])})

    doc_ref = db.collection(u'hospitals').where(u'name', u'==', user).stream()
    items=[]
    for doc in doc_ref:
        items.append(doc.to_dict())
        
    return render(request,"hospiProfile.html", {'content': items})