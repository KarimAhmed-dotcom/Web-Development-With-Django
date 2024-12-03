from django.urls import path 
from . import views 


app_name="mytasks" 

urlpatterns=[
    path("",views.index,name="index"),
    path("add",views.addtasks,name="addtasks")
]