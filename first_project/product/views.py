from django.shortcuts import render
from .models import userinfo
from django.http import HttpResponse
def call(r):
    return render(r,'product.html')

def userInfo(request):
    usr = userinfo(
        name = request.POST['na'],
        email = request.POST['em'],
        password = request.POST['pa'],
        phone = request.POST['ph']
    )
    usr.save()
    return HttpResponse("User Saved!!")