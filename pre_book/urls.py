from django.urls import path
from . import views

urlpatterns = [
    path('pre_book',views.pre_book,name='pre_book'),
    path('update(?p<disease>\w+)/(?P<hospital>\w+)/(?P<mobile>\w+)/(?P<preBook_date>\w+)$',views.update,name = 'update'),
]
