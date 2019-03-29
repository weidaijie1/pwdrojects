from django.shortcuts import render

# Create your views here.
import  datetime
from django.shortcuts import  render,redirect


def redistest(request):
    t = datetime.datetime.now()
	print('hahahah')
	print（'我写了一个程序'）

    return render(request,'redis.html',{'t':t})