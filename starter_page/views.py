# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Article, PageSection
import datetime

def home(request):
  latest_article = Article.objects.order_by('-published').first()
  welcome = PageSection.objects.filter(name="welcome").first()
  about = PageSection.objects.filter(name="about").first()

  context = {
        "latest_article" : latest_article,
        "welcome": welcome,
        "about": about,
        "site_name": "N8than's Stash",
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

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    past_articles = Article.objects.exclude(id=article.id).order_by('-published')[:10]
    context = {
      "article": article,
      "past_articles": past_articles,
      "current_year": datetime.date.today().year,
    }
    return render(request, "article.html", context)
