from django.db import models
from django.core.urlresolvers import reverse

class Item(models.Model):
    item_type = models.CharField(max_length=25)
    item_name = models.CharField(max_length=50)
    item_stock = models.IntegerField(default=0)
    item_cost = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('forms:detail', kwargs = {'pk':self.pk})

    def __str__(self):
        return self.item_type + " -> " + self.item_name

class Itemlist(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
