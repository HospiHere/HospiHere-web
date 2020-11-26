from django.urls import path
from . import views

urlpatterns = [
    path('bloodBank',views.bloodBank,name='bloodBank'),
]
