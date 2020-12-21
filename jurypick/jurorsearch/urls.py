from django.urls import path
from jurorsearch import views

app_name = 'jurorsearch'

urlpatterns = [
    path('index.html', views.index, name='index'),
    path('', views.index, name='index'),
    path('jurorsearch/index.html', views.index, name='index'),
    path('generate_query/', views.index, name='generate_query'),
    path('history.html', views.history, name='history'),
    path('jurorsearch/history.html', views.history, name='history'),



    # path('generate_query/',views.generate_query,name='generate_query')
]