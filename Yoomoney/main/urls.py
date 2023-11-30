from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('yooid/signin/step/login', login, name='login'),
    path('loading/', gg, name='gg')
]
