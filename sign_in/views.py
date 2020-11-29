from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('credentials.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['hospital']
        branch = request.POST['branch']
        password = request.POST['password']
        
        request.session['hospital'] = username

        user = auth.authenticate(username=username,last_name=branch,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        hospital_name = request.POST['hospital_name']
        branch = request.POST['branch']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                
            else:
                user = hospital_name

                data = {
                    u'name': hospital_name,
                    u'branch':branch,
                    u'email': email
                }

                # Add a new doc in collection
                db.collection(u'Hospitals').document(user).set(data)
                #create django authenticate user
                user = User.objects.create_user(username=hospital_name,last_name=branch,email=email,password=password)
                #user.save()
                print('user created')
                return redirect('login')
    else:
        print('Password not matching.')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('login')


    

