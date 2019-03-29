from django.shortcuts import render

# Create your views here.
import  datetime
from django.shortcuts import  render,redirect


def redistest(request):
    t = datetime.datetime.now()

    return render(request,'redis.html',{'t':t})