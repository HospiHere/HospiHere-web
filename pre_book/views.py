from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Create your views here.
db = firestore.client()

def pre_book(request):
    user = request.user.username
    doc_ref = db.collection(u'booking').where(u'hospital', u'==', user).stream()
    items=[]
    for doc in doc_ref:
        items.append(doc.to_dict())
    return render(request,"pre_book.html", {'content': items})

def update(request, hospital, mobile, preBook_date):
    db.collection(u'booking').document(hospital + '-' + mobile + '-' + preBook_date).update({
    "status": "confirm"
    })

    user = request.user.username
    doc_ref = db.collection(u'booking').where(u'hospital', u'==', user).stream()
    items=[]
    for doc in doc_ref:
        items.append(doc.to_dict())
    return render(request,"pre_book.html", {'content': items})

    