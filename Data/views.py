from django.shortcuts import render
from Data import models

# Create your views here.

def Home(request):
    if request.method == 'GET':
        temp = request.GET.get('temp')
        humi = request.GET.get('humi')
        a=models.Data(temp=temp,humi=humi)
        a.save()
    return render(request, 'Home.html')


