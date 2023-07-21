from django.urls import path

from app2.views import *
app_name='again me only'

urlpatterns = [
    path('first_app2/',first_app2,name='first_app2')
]
