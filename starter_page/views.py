# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Member
import datetime

def home(request):
  context = {
        "site_name": "My Personal Website",
        "current_year": datetime.date.today().year,
        "user": request.user,
        "latest_video_id": "mWJuPvOIzYA",  # Replace with dynamic YT video ID
    }
  return render(request, "home.html", context)

def about(request):
  return render(request, "about.html")

def contact(request):
  return render(request, "contact.html")

def page404(request):
  context = {
        "current_year": datetime.date.today().year,
    }
  return render(request, "404.html", context)
