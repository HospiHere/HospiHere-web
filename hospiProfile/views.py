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
        
    return render(request,"hospiProfile.html",)