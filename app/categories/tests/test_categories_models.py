import pytest


class TestCategoryModel:
    @pytest.mark.django_db(transaction=True)
    def test_model(self, python_category):
        inst = python_category
        assert inst.pk
        assert inst.__str__()
        assert inst.delete()
