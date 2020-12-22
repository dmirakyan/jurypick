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

#  APIs
    path('api',views.apiOverview, name="api-overview"),
    path('api/human-list/',views.humanList, name="human-list"),
    path('api/human-details/<int:pk>/',views.humanDetails, name="human-details"),
    path('api/human-update/<int:pk>/',views.humanUpdate, name="human-update"),
    # path('api/human-hide/<int:pk>/',views.humanHide, name="human-hide"),

    path('api/human-hide/<int:pk>/',views.hideHuman, name="human-hide"),
    
    path('api/human-star/<int:pk>/',views.starHuman, name="human-star"),






    # path('generate_query/',views.generate_query,name='generate_query')
]