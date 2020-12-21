from django.urls import path
from . import views

urlpatterns = [
    path('hospiProfile',views.hospiProfile,name='hospiProfile'),
    path('branch',views.branch,name='branch'),
    path('email',views.email,name='email'),
    path('bed',views.bed,name='bed'),
]
