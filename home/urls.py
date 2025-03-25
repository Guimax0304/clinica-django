#home/urls.py

from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    # Rota principal da home, que renderiza o template HTML
    path('', views.home, name='home'),
]