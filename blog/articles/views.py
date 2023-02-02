from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.

class ArticleList(ListView):
	model=Article
	template_name='base.html'

class ArticleDetailView(DetailView):
	model=Article
	template_name='detail.html'