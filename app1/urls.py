from django.urls import path
from app1.views import *

app_name='hi there'

urlpatterns = [
    path('first/',first,name='first'),
    path('second_app1/',second_app1,name='second_app1'),
    path('third_app1/',third_app1,name='third_app1'),
]
