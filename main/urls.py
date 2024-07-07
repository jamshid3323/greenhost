from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('domain/', DomainView.as_view(), name='domain'),

]