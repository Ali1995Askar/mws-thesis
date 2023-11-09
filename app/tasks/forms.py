from django import forms

from categories.models import Category
from educations.models import Education
from tasks.models import Task


class MultiSelectTagField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class TaskForm(forms.ModelForm):
    # level = forms.ChoiceField(choices=Task.Level.choices)
    categories = MultiSelectTagField(required=False, queryset=Category.objects.all())
    educations = MultiSelectTagField(required=False, queryset=Education.objects.all())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        self.fields['title'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'name': 'title',
            'id': 'title',
        })

        self.fields['description'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'name': 'description',
            'id': 'description',
        })

        self.fields['deadline'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'name': 'deadline',
            'id': 'deadline',
        })

        self.fields['status'].widget = forms.Select(
            choices=Task.Status.choices,
            attrs={
                'class': 'form-control',
                'name': 'status',
                'id': 'status',
            })

        self.fields['categories'].widget = forms.SelectMultiple(
            choices=Category.objects.filter(user=user).values_list('id', 'name'),
            attrs={
                'class': 'form-control',
                'name': 'categories',
                'id': 'categories',
            })

        self.fields['educations'].widget = forms.SelectMultiple(
            choices=Education.objects.filter(user=user).values_list('id', 'name'),
            attrs={
                'class': 'form-control',
                'name': 'educations',
                'id': 'educations',
            })

    class Meta:
        model = Task
        exclude = ['user']
