from django.shortcuts import render
from django.http import HttpResponse
from app.froms import *
from app.models import *
# Create your views here.
def insert_student(request):
    SFEO=StudentForms()
    d={'SFEO':SFEO}
    if request.method=='POST':
        SFDO=StudentForms(request.POST)

        if SFDO.is_valid():
            Sname=SFDO.cleaned_data['Sname']
            Sid=SFDO.cleaned_data['Sid']
            Semail=SFDO.cleaned_data['Semail']
            SO=Student.objects.get_or_create(Sname=Sname,Sid=Sid,Semail=Semail)[0]
            SO.save()

            SFO=Student.objects.all()
            d1={'SFO':SFO}
            return render(request,'display_student.html',d1)




            
    return render(request,'insert_student.html',d)