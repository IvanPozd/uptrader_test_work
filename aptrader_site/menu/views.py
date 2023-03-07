from django.shortcuts import render, get_object_or_404
from .models import MenuItem

# Create your views here


def menu_item_detail(request):
    return render(request, 'menu_item_detail.html')
