from django.urls import path
from . import views

app_name = 'myguestbook'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new/', views.NewView.as_view(), name='new')
]
