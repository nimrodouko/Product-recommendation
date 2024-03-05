from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import *
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class ElectronicView(ListView):
    model = Electronics
    template_name = 'electronics.html'

class ClothingView(ListView):
    model = Clothing
    template_name = 'clothing.html'


class FurnitureView(ListView):
    model = Furniture
    template_name = 'furniture.html'