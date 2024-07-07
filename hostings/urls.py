from django.urls import path
from .views import *

app_name = 'hosting'

urlpatterns = [
    path('', HostingView.as_view(), name='hosting'),

]
