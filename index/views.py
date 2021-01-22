from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = 'base/index.html'


class HomeView(TemplateView):
    template_name = 'base/base.html'