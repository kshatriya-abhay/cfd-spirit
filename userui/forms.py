from django import forms

from .models import Item

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('item_name', 'item_type',)