import pytest


class TestEducationModel:
    @pytest.mark.django_db(transaction=True)
    def test_model(self, it_education):
        inst = it_education
        assert inst.pk
        assert inst.__str__()
        inst.delete()
