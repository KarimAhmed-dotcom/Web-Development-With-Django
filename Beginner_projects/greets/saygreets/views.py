from django.shortcuts import render

# Create your views here.

def greets(request,name) : 
    return render(request,"saygreets/greets.html",{
        "name":name.capitalize()
    })