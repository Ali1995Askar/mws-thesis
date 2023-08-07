from django import forms
from management.models import ContactUs


class ContactUsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'name': 'name',
            'id': 'name',
            'placeholder': "Your Name"
        })

        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control',
            'type': 'email',
            'name': 'email',
            'id': 'email',
            'placeholder': "Your Email"
        })

        self.fields['subject'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'name': 'subject',
            'id': 'subject',
            'placeholder': "Subject"
        })

        self.fields['message'].widget = forms.Textarea(attrs={
            'class': 'form-control',
            'type': 'text',
            'name': 'message',
            'id': 'message',
            'rows': "5",
            'placeholder': "Message"
        })

    class Meta:
        model = ContactUs
        fields = "__all__"
