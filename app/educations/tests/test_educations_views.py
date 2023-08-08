import pytest

from django.urls import reverse

from educations.models import Education


class TestEducationListView:
    url = reverse('educations:list')

    @pytest.mark.django_db(transaction=True)
    def test_post(self, authorized_client, un_authorized_client):
        response = authorized_client.post(self.url)
        assert response.status_code == 405

        response = un_authorized_client.post(self.url)
        assert response.status_code == 302
        redirected_url = response.url
        assert redirected_url == '/accounts/signin?next=/educations/'

    @pytest.mark.django_db(transaction=True)
    def test_get(self, svu_user, network_education, it_education, authorized_client, un_authorized_client):
        response = un_authorized_client.get(self.url)
        assert response.status_code == 302
        redirected_url = response.url
        assert redirected_url == '/accounts/signin?next=/educations/'

        response = authorized_client.get(self.url)

        assert "<td>it</td>" in response.content.decode()
        assert "<td>network</td>" in response.content.decode()

        it_education.user = svu_user
        it_education.save()

        response = authorized_client.get(self.url)
        assert "<td>network</td>" in response.content.decode()
        assert "<td>it</td>" not in response.content.decode()

        network_education.user = svu_user
        network_education.save()

        response = authorized_client.get(self.url)
        assert "<td>it</td>" not in response.content.decode()
        assert "<td>network</td>" not in response.content.decode()


class TestEducationCreateView:
    url = reverse('educations:create')

    @pytest.mark.django_db(transaction=True)
    def test_post(self, authorized_client, un_authorized_client):
        response = un_authorized_client.post(self.url)
        assert response.status_code == 302
        redirected_url = response.url
        assert redirected_url == '/accounts/signin?next=/educations/create'

        form_data = {'name': 'education'}
        response = un_authorized_client.post(self.url, form_data)
        redirected_url = response.url
        assert redirected_url == '/accounts/signin?next=/educations/create'

        assert Education.objects.all().count() == 0
        response = authorized_client.post(self.url, form_data)
        assert Education.objects.all().count() == 1
        assert response.url == '/educations/'
        assert Education.objects.all().first().name == 'education'

    @pytest.mark.django_db(transaction=True)
    def test_get(self, authorized_client, un_authorized_client):
        response = un_authorized_client.get(self.url)
        assert response.status_code == 302
        assert 'response.url = /accounts/signin?next=/educations/create'

        response = authorized_client.get(self.url)
        assert response.status_code == 200
        assert 'Education Form' in response.content.decode()


class TestEducationUpdateView:

    @pytest.mark.django_db(transaction=True)
    def test_post(self, svu_user, authorized_client, it_education, un_authorized_client):
        url = reverse('educations:update', args=[it_education.id])
        form_data = {'name': 'new_name'}
        assert it_education.name != 'new_name'
        response = authorized_client.post(url, form_data)
        assert response.status_code == 302
        it_education.refresh_from_db()
        assert it_education.name == 'new_name'

        it_education.user = svu_user
        it_education.save()
        response = authorized_client.post(url, form_data)
        print(response.content.decode())
        assert response.status_code == 404

    @pytest.mark.django_db(transaction=True)
    def test_get(self, svu_user, authorized_client, un_authorized_client, it_education):
        url = reverse('educations:update', args=[it_education.id])

        response = un_authorized_client.get(url)
        assert response.status_code == 302
        assert response.url == f'/accounts/signin?next=/educations/update/{it_education.id}'

        response = authorized_client.get(url)
        assert response.status_code == 200
        assert 'Update Education' in response.content.decode()
        assert it_education.name in response.content.decode()

        it_education.user = svu_user
        it_education.save()

        response = authorized_client.get(url)
        assert response.status_code == 404


class TestEducationDeleteView:
    @pytest.mark.django_db(transaction=True)
    def test_post(self, authorized_client, un_authorized_client, it_education):
        url = reverse('educations:delete', args=[it_education.id])
        assert Education.objects.all().count() == 1
        response = authorized_client.post(url)
        assert response.status_code == 302

        assert Education.objects.all().count() == 0
        response = authorized_client.post(url)
        assert response.status_code == 404

        response = un_authorized_client.post(url)
        assert response.status_code == 302
        assert response.url == f'/accounts/signin?next=/educations/delete/{it_education.id}'

    @pytest.mark.django_db(transaction=True)
    def test_get(self, svu_user, authorized_client, un_authorized_client, it_education, network_education):
        url = reverse('educations:delete', args=[it_education.id])

        response = un_authorized_client.get(url)
        assert response.status_code == 302
        assert response.url == f'/accounts/signin?next=/educations/delete/{it_education.id}'

        response = authorized_client.get(url)
        assert response.status_code == 200
        assert 'Delete Education' in response.content.decode()
        assert it_education.name in response.content.decode()

        it_education.user = svu_user
        it_education.save()

        response = authorized_client.get(url)
        assert response.status_code == 404

        network_education.user = svu_user
        network_education.save()

        url = reverse('educations:delete', args=[network_education.id])
        response = authorized_client.get(url)
        assert response.status_code == 404
