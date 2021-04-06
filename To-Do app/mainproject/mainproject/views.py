from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import classtodo

# Create your views here.

def todoview(request):
    all_todo=classtodo.objects.all() #after models migrate get all objects from 000_initial.py
    return render(request,'base.html',{'items':all_todo})

def addtodo(request):
    newdata = classtodo(data = request.POST['data'])
    newdata.save()
    return HttpResponseRedirect('/todo/')
def deletetodo(request,item_id):
    temp=classtodo.objects.get(id=item_id)
    temp.delete()
    return HttpResponseRedirect('/todo/')