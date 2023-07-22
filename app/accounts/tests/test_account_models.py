import pytest

from accounts.models import Profile


class TestProfileModel:
    @pytest.mark.django_db(transaction=True)
    def test_model(self, pytech_user):
        assert Profile.objects.all().count() == 1
        inst = pytech_user
        assert inst.pk
        assert inst.__str__()
        assert inst.profile

        inst.save()
        assert Profile.objects.all().count() == 1

        inst.delete()
        assert Profile.objects.all().count() == 0
