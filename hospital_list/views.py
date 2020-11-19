from django.shortcuts import render
from django.http import HttpResponse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
#cred = credentials.Certificate('credentials.json')
#firebase_admin.initialize_app(cred)

db = firestore.client()

# Create your views here.
def hospital_list(request):
    items = []
    users_ref = db.collection(u'hospitals')
    docs = users_ref.stream()

    for doc in docs:
        items.append(doc.to_dict())

    return render(request,"hospital_list.html", {'content': items})