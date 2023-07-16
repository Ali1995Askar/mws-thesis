from django import forms
from categories.models import Category


class CategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'name': 'name',
            'id': 'name',
        })

    class Meta:
        model = Category
        fields = ['name', ]
