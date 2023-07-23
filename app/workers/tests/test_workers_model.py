import pytest


class TestTasKSModel:
    @pytest.mark.django_db(transaction=True)
    def test_model(self, worker_ali_askar):
        inst = worker_ali_askar
        assert inst.pk
        assert inst.__str__()
        inst.delete()

    def test_signal_dispatch(self):
        pass
