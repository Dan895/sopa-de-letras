from django.urls import path
from .views import home, about, GenerarSopa

app_name = 'sopa'

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('nuevasopa', GenerarSopa, name='nuevasopa'),
]
