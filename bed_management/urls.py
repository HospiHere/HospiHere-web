from django.urls import path
from . import views

urlpatterns = [
    path('bed_management',views.bed_management,name='bed_management'),
]
