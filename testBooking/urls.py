from django.urls import path
from . import views

urlpatterns = [
    path('testBooking',views.testBooking,name='testBooking'),
    path('update(?p<testName>\w+)/(?P<hospital>\w+)/(?P<mobile>\w+)/(?P<testAppointmentDate>\w+)/(?P<testAppointmentTime>\w+)$',views.update,name = 'update'),
]
