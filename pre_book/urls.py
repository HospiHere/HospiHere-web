from django.urls import path
from . import views

urlpatterns = [
    path('pre_book',views.pre_book,name='pre_book'),
    path('update(?P<hospital>\w+)/(?P<mobile>\w+)/(?P<disease>\w+)/(?P<preBook_date>\w+)$',views.update,name = 'update'),
]
