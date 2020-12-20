from django.urls import path
from . import views

urlpatterns = [
    path('hospiProfile',views.hospiProfile,name='hospiProfile'),
]
