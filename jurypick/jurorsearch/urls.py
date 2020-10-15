from django.urls import path
from jurorsearch import views

app_name = 'jurorsearch'

urlpatterns = [
    path('', views.index, name='index'),
]