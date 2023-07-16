from django import forms
from categories.models import Category
from departments.models import Department


class CategoryForm(forms.ModelForm):
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')

        super().__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'name': 'name',
            'id': 'name',
        })
        self.fields['department'].queryset = Department.objects.filter(user=user)

    class Meta:
        model = Category
        fields = ['name', 'department']
