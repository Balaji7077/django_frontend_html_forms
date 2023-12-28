from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def html_forms(request):
    if request.method == 'POST':
        username = request.POST['un']
        return HttpResponse(username)
    return render(request,'html_forms.html')

def create_school(request):
    if request.method == 'POST':
        Sname = request.POST['Sn']
        Slocation = request.POST['Sl']
        Sprinciple = request.POST['Sp']

        we=school.objects.get_or_create(Sname=Sname,Slocation=Slocation,Sprinciple=Sprinciple)[0]
        we.save()
        return HttpResponse('data submited succsessfully')

    return render(request,'create_school.html')