from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Item
from django.core.urlresolvers import reverse_lazy

class IndexView(generic.ListView):
    model = Item
    template_name = 'index.html'
    context_object_name = 'all_items'

    def get_queryset(self):
        return Item.objects.all()

class DetailView(generic.DetailView):
    model = Item
    template_name = 'detail.html'

class ItemCreate(CreateView):
    model = Item
    fields = ['item_name','item_type','item_cost', 'item_stock']

class ItemUpdate(UpdateView):
    model = Item
    fields = ['item_cost', 'item_stock']

class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('test')