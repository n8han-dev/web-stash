# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def hello(request):
    data = Member.objects.all().values()
    page = loader.get_template('test.html')
    vars = {
        'mymembers': data,
    }
    return HttpResponse(page.render(vars, request))

def details(request, id):
  data = Member.objects.get(id=id)
  page = loader.get_template('details.html')
  vars = {
    'mymember': data,
  }
  return HttpResponse(page.render(vars, request))

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))
