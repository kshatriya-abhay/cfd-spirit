from django.http import HttpResponse
from django.shortcuts import render
from forms.models import Item

def index(request):
    all_items = Item.objects.all()
    context = {'all_items' : all_items}
    return render(request, 'userui/index.html', context)
