import pytest

from django.urls import reverse

from categories.models import Category


class TestCategoryListView:
    url = reverse('categories:list')

    @pytest.mark.django_db(transaction=True)
    def test_post(self, authorized_client, un_authorized_client):
        response = authorized_client.post(self.url)
        assert response.status_code == 405

        response = un_authorized_client.post(self.url)
        assert response.status_code == 302
        redirected_url = response.url
        assert redirected_url == '/accounts/signin?next=/categories/'

    @pytest.mark.django_db(transaction=True)
    def test_get(self, svu_user, aws_category, marketing_category, authorized_client, un_authorized_client):
        response = un_authorized_client.get(self.url)
        assert response.status_code == 302
        redirected_url = response.url
        assert redirected_url == '/accounts/signin?next=/categories/'

        response = authorized_client.get(self.url)

        assert "<td>marketing</td>" in response.content.decode()
        assert "<td>aws</td>" in response.content.decode()

        aws_category.user = svu_user
        aws_category.save()

        response = authorized_client.get(self.url)
        assert "<td>marketing</td>" in response.content.decode()
        assert "<td>aws</td>" not in response.content.decode()

        marketing_category.user = svu_user
        marketing_category.save()

        response = authorized_client.get(self.url)
        assert "<td>marketing</td>" not in response.content.decode()
        assert "<td>aws</td>" not in response.content.decode()


class TestCategoryCreateView:
    url = reverse('categories:create')

    @pytest.mark.django_db(transaction=True)
    def test_post(self, authorized_client, un_authorized_client):
        response = un_authorized_client.post(self.url)
        assert response.status_code == 302
        redirected_url = response.url
        assert redirected_url == '/accounts/signin?next=/categories/create'

        form_data = {'name': 'category'}
        response = un_authorized_client.post(self.url, form_data)
        redirected_url = response.url
        assert redirected_url == '/accounts/signin?next=/categories/create'

        assert Category.objects.all().count() == 0
        response = authorized_client.post(self.url, form_data)
        assert Category.objects.all().count() == 1
        assert response.url == '/categories/'
        assert Category.objects.all().first().name == 'category'

    @pytest.mark.django_db(transaction=True)
    def test_get(self, authorized_client, un_authorized_client):
        response = un_authorized_client.get(self.url)
        assert response.status_code == 302
        assert 'response.url = /accounts/signin?next=/categories/create'

        response = authorized_client.get(self.url)
        assert response.status_code == 200
        assert 'Category Form' in response.content.decode()


class TestCategoryUpdateView:

    @pytest.mark.django_db(transaction=True)
    def test_post(self, svu_user, authorized_client, aws_category, un_authorized_client):
        url = reverse('categories:update', args=[aws_category.id])
        form_data = {'name': 'new_name'}
        assert aws_category.name != 'new_name'
        response = authorized_client.post(url, form_data)
        assert response.status_code == 302
        aws_category.refresh_from_db()
        assert aws_category.name == 'new_name'

        aws_category.user = svu_user
        aws_category.save()

        response = authorized_client.post(url, form_data)
        assert response.status_code == 404

        response = un_authorized_client.post(url, form_data)
        assert response.status_code == 302
        assert response.url == f'/accounts/signin?next=/categories/update/{aws_category.id}'

    @pytest.mark.django_db(transaction=True)
    def test_get(self, svu_user, authorized_client, un_authorized_client, aws_category):
        url = reverse('categories:update', args=[aws_category.id])

        response = un_authorized_client.get(url)
        assert response.status_code == 302
        assert response.url == f'/accounts/signin?next=/categories/update/{aws_category.id}'

        response = authorized_client.get(url)
        assert response.status_code == 200
        assert 'Update Category' in response.content.decode()
        assert aws_category.name in response.content.decode()

        aws_category.user = svu_user
        aws_category.save()

        response = authorized_client.get(url)
        assert response.status_code == 404


class TestCategoryDeleteView:
    @pytest.mark.django_db(transaction=True)
    def test_post(self, svu_user, authorized_client, aws_category, un_authorized_client):
        url = reverse('categories:delete', args=[aws_category.id])
        assert Category.objects.all().count() == 1
        response = authorized_client.post(url)
        assert response.status_code == 302

        assert Category.objects.all().count() == 0
        response = authorized_client.post(url)
        assert response.status_code == 404

        response = un_authorized_client.post(url)
        assert response.status_code == 302
        assert response.url == f'/accounts/signin?next=/categories/delete/{aws_category.id}'

    @pytest.mark.django_db(transaction=True)
    def test_get(self, svu_user, authorized_client, un_authorized_client, aws_category):
        url = reverse('categories:delete', args=[aws_category.id])

        response = un_authorized_client.get(url)
        assert response.status_code == 302
        assert response.url == f'/accounts/signin?next=/categories/delete/{aws_category.id}'

        response = authorized_client.get(url)
        assert response.status_code == 200
        assert 'Delete Category' in response.content.decode()
        assert aws_category.name in response.content.decode()

        aws_category.user = svu_user
        aws_category.save()

        response = authorized_client.get(url)
        assert response.status_code == 404
