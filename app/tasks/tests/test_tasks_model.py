import pytest


class TestTasKSModel:
    @pytest.mark.django_db(transaction=True)
    def test_model(self, task_fix_tests):
        inst = task_fix_tests
        assert inst.pk
        assert inst.__str__()
        inst.delete()

    def test_signal_dispatch(self):
        pass
