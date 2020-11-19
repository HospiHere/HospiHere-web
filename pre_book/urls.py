from django.urls import path
from . import views

urlpatterns = [
    path('pre_book',views.pre_book,name='pre_book'),
]
