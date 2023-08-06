import pytest
from django.urls import reverse
from django.http import HttpResponse


class TestSigninView:
    url = reverse('accounts:signin')

    @pytest.mark.django_db(transaction=True)
    def test_get_signin_view(self, un_authorized_client, authorized_client):
        response: HttpResponse = un_authorized_client.get(self.url)
        assert response.status_code == 200
        assert "Login to Your Account" in response.content.decode()

        response = authorized_client.get(self.url)
        assert response.status_code == 302
        redirected_url = response.url
        assert redirected_url == '/'

    @pytest.mark.django_db(transaction=True)
    def test_post_signin_view(self, pytech_user, un_authorized_client, authorized_client):
        form_data = {
            'username': 'value1',
            'password': 'value2',
        }
        response = un_authorized_client.post(self.url, form_data)
        assert "Login to Your Account" in response.content.decode()

        form_data = {
            'username': pytech_user.username,
            'password': 'new_password',

        }

        response = un_authorized_client.post(self.url, form_data)
        redirected_url = response.url
        assert redirected_url == '/management/dashboard'

        response = authorized_client.post(self.url, form_data)
        redirected_url = response.url
        assert redirected_url == '/'


class TestSignupView:
    url = reverse('accounts:signup')

    @pytest.mark.django_db(transaction=True)
    def test_get_signup_view(self, un_authorized_client, authorized_client):
        response: HttpResponse = un_authorized_client.get(self.url)
        assert response.status_code == 200
        assert "Create an Account" in response.content.decode()

        response = authorized_client.get(self.url)
        assert response.status_code == 302
        redirected_url = response.url
        assert redirected_url == '/'

    @pytest.mark.django_db(transaction=True)
    def test_post_signup_view(self, un_authorized_client, authorized_client):
        form_data = {
            'username': 'ali',
            'email': 'ali@ali.com',
            'password1': 'password1',
            'password2': 'password2',
        }
        response = un_authorized_client.post(self.url, form_data)
        assert "Create an Account" in response.content.decode()
        assert "The two password" in response.content.decode()

        form_data = {
            'username': 'ali',
            'email': 'ali@ali.com',
            'password1': 'password123Password',
            'password2': 'password123Password',
        }
        response = un_authorized_client.post(self.url, form_data)
        assert response.status_code == 302
        redirected_url = response.url
        assert redirected_url == "/accounts/profile"

        response = authorized_client.post(self.url, form_data)
        redirected_url = response.url
        assert redirected_url == '/'


class TestLogoutView:
    url = reverse('accounts:logout')

    @pytest.mark.django_db(transaction=True)
    def test_get_logout_view(self, un_authorized_client, authorized_client):
        response: HttpResponse = un_authorized_client.get(self.url)
        redirected_url = response.url
        assert response.status_code == 302
        assert redirected_url == "/accounts/signin?next=/accounts/logout"

        response: HttpResponse = authorized_client.get(self.url)
        assert response.status_code == 200
        assert "Are you sure you want to Logout" in response.content.decode()

    @pytest.mark.django_db(transaction=True)
    def test_post_logout_view(self, un_authorized_client, authorized_client):
        response: HttpResponse = un_authorized_client.post(self.url)
        redirected_url = response.url
        assert response.status_code == 302
        assert redirected_url == "/accounts/signin?next=/accounts/logout"

        response: HttpResponse = authorized_client.post(self.url)
        redirected_url = response.url
        assert redirected_url == "/"


class TestChangePasswordView:
    url = reverse('accounts:change-password')

    @pytest.mark.django_db(transaction=True)
    def test_post_change_password_view(self, pytech_user, un_authorized_client, authorized_client):
        form_data = {
            'old_password': '',
            'new_password1': '',
            'new_password2': ''
        }
        response: HttpResponse = un_authorized_client.post(self.url, form_data)
        redirected_url = response.url
        assert response.status_code == 302
        assert redirected_url == '/accounts/signin?next=/accounts/change-password'

        response: HttpResponse = authorized_client.post(self.url, form_data)
        assert response.status_code == 400

        form_data = {
            'old_password': 'new_password_2',
            'new_password1': 'new_password_2',
            'new_password2': 'new_password_2'
        }

        response: HttpResponse = authorized_client.post(self.url, form_data)
        assert response.status_code == 400

        response: HttpResponse = authorized_client.post(self.url, form_data)
        assert response.status_code == 400

        form_data['old_password'] = 'new_password'

        logged_in = authorized_client.login(username=pytech_user.username, password="new_password")
        assert logged_in is True
        response: HttpResponse = authorized_client.post(self.url, form_data)
        assert response.status_code == 200
        logged_in = authorized_client.login(username=pytech_user.username, password="new_password")
        assert logged_in is False
        logged_in = authorized_client.login(username=pytech_user.username, password="new_password_2")
        assert logged_in is True


class TestEditProfileView:
    url = reverse('accounts:edit-profile')

    @pytest.mark.django_db(transaction=True)
    def test_post_edit_profile_view(self, pytech_user, un_authorized_client, authorized_client):
        form_data = {}

        response: HttpResponse = un_authorized_client.post(self.url, form_data)
        assert response.status_code == 302
        redirected_url = response.url
        assert redirected_url == '/accounts/signin?next=/accounts/edit-profile'

        response: HttpResponse = authorized_client.post(self.url, form_data)
        assert response.status_code == 200
        assert pytech_user.profile.name is None
        assert pytech_user.profile.about is None
        assert pytech_user.profile.address is None
        assert pytech_user.profile.phone_number is None
        assert pytech_user.profile.contact_email is None

        form_data = {
            'name': 'SVU',
            'about': 'MASTER',
            'address': 'Syria Damascus',
            'phone_number': '00971543267404',
            'contact_email': 'contact@gmail.com'
        }
        response: HttpResponse = authorized_client.post(self.url, form_data)
        assert response.status_code == 200
        pytech_user.profile.refresh_from_db()
        pytech_user.refresh_from_db()
        assert pytech_user.profile.name == 'SVU'
        assert pytech_user.profile.about == 'MASTER'
        assert pytech_user.profile.address == 'Syria Damascus'
        assert pytech_user.profile.phone_number == '00971543267404'
        assert pytech_user.profile.contact_email == 'contact@gmail.com'
