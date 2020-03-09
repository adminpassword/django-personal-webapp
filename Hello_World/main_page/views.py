from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View


# Create your views here.

class HomePageView(TemplateView):
    template_name = "base.html"


class PhpPageView(TemplateView):
    template_name = 'main_page/crud.html'
