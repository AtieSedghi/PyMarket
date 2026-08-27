from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def index(request):
    goods=Item.objects.all()
    return render(request, "index.html",
                  {"products":goods})
def new_product(request):
    return HttpResponse("Trends")
