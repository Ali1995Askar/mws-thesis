from django import forms
from workers.models import Worker
from categories.models import Category
from educations.models import Education


class MultiSelectTagField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class WorkerForm(forms.ModelForm):
    # level = forms.ChoiceField(choices=Task.Level.choices)
    categories = MultiSelectTagField(required=False, queryset=Category.objects.all())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'name': 'first_name',
            'id': 'first_name',
        })

        self.fields['last_name'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'name': 'last_name',
            'id': 'last_name',
        })

        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control',
            'type': 'email',
            'name': 'email',
            'id': 'email',
        })

        self.fields['level'].widget = forms.Select(
            choices=Worker.Level.choices,
            attrs={
                'class': 'form-control',
                'name': 'level',
                'id': 'level',
            })

        self.fields['status'].widget = forms.Select(
            choices=Worker.Status.choices,
            attrs={
                'class': 'form-control',
                'name': 'status',
                'id': 'status',
            })

        self.fields['categories'].widget = forms.SelectMultiple(
            choices=Category.objects.all().values_list('id', 'name'),
            attrs={
                'class': 'form-control',
                'name': 'categories',
                'id': 'categories',
                'required': False
            })

        self.fields['education'].widget = forms.Select(
            choices=Education.objects.filter(user=user).values_list('id', 'name'),
            attrs={
                'class': 'form-control',
                'name': 'education',
                'id': 'education',
            })

    class Meta:
        model = Worker
        exclude = ['user']
