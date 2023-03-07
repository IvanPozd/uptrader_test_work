from django import forms
from .models import MenuItem


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['title', 'parent', 'url', 'named_url', 'menu']

    def clean_url(self):
        return self.cleaned_data['url'] or None

    def clean_named_url(self):
        return self.cleaned_data['named_url'] or None

    def clean_menu(self):
        return self.cleaned_data['menu'] or None