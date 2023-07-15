from django import forms
from departments.models import Department


class DepartmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'name': 'name',
            'id': 'name',
        })

    class Meta:
        model = Department
        fields = ['name']
