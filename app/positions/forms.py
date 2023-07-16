from django import forms
from positions.models import Position
from categories.models import Category
from educations.models import Education


class PositionForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    education = forms.ModelChoiceField(
        queryset=Education.objects.all(),
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
        self.fields['category'].queryset = Category.objects.filter(user=user)
        self.fields['education'].queryset = Education.objects.filter(user=user)

    class Meta:
        model = Position
        fields = ['name', 'category', 'education']
