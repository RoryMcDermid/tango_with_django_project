from django.urls import path
from rango import views


app_name = 'rango'
urlpatterns = [
    path('about/', views.index, name='index'),
    path('test/', views.test, name = 'test')
]
