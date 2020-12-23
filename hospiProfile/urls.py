from django.urls import path
from . import views

urlpatterns = [
    path('hospiProfile',views.hospiProfile,name='hospiProfile'),
    path('branch',views.branch,name='branch'),
    path('email',views.email,name='email'),
    path('latitude',views.latitude,name='latitude'),
    path('bed',views.bed,name='bed'),
    path('test',views.test,name='test'),
    path('remove(?P<test>\w+)$',views.remove,name='remove'),
    path('specialized',views.specialized,name='specialized'),
    path('removeSp(?P<specialized>\w+)$',views.removeSp,name='removeSp'),
]
