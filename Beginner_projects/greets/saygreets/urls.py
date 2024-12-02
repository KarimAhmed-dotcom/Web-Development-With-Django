from django.urls import path 
from . import views

app_name="saygreets"

urlpatterns=[
    path("<str:name>",views.greets,name="saygreet")
]