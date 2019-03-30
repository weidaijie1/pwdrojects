from django.shortcuts import render

# Create your views here.
import  datetime
from django.shortcuts import  render,redirect


def redistest(request):
    t = datetime.datetime.now()
	print('hahahah')
	print(qqq)
	print('我是ddb，这是我开发的项目')
    return render(request,'redis.html',{'t':t})