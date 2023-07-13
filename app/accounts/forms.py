from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.forms import AuthenticationForm

from accounts.models import Profile


class SignupForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize widget for an existing field

        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'name': 'name',
            'id': 'companyName',
        })

        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control',
            'type': 'email',
            'name': 'email',
            'id': 'companyEmail',
        })

        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'Password1',
            'name': 'Password1',
            'id': 'Password1',
        })

        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'Password2',
            'name': 'Password2',
            'id': 'Password2',
        })


class SigninForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'name': 'name',
            'id': 'companyName',
        })

        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'Password',
            'name': 'Password',
            'id': 'Password',
        })


class ChangePasswordForm(PasswordChangeForm):

    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)

        self.fields['old_password'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'name': 'old_password',
            'id': 'old_password',
        })

        self.fields['new_password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'name': 'new_password1',
            'id': 'new_password1',
        })

        self.fields['new_password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'name': 'new_password2',
            'id': 'new_password2',
        })


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['contact_email'].widget = forms.EmailInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'name': 'contact_email',
            'id': 'contact_email',
            'value': self.instance.contact_email or ''
        })

        self.fields['address'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'name': 'address',
            'id': 'address',
            'value': self.instance.address or ''
        })

        self.fields['name'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'name': 'name',
            'id': 'name',
            'style': '"height: 100px"',
            'value': self.instance.name or ''
        })

        self.fields['about'].widget = forms.Textarea(attrs={
            'class': 'form-control',
            'type': 'text',
            'name': 'about',
            'id': 'about',
            'value': self.instance.about or ''

        })

        self.fields['phone_number'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'name': 'phone_number',
            'id': 'phone_number',
            'value': self.instance.phone_number or ''
        })

    class Meta:
        model = Profile
        fields = ['name', 'address', 'contact_email', 'about', 'phone_number']
