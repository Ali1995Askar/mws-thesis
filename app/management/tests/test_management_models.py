import pytest


class TestHeuristicMatchingModel:
    @pytest.mark.django_db(transaction=True)
    def test_model(self, heuristic_matching_1):
        inst = heuristic_matching_1
        assert inst.pk
        assert inst.__str__()
        inst.delete()


class TestMaxMatchingModel:
    @pytest.mark.django_db(transaction=True)
    def test_model(self, max_matching_1):
        inst = max_matching_1
        assert inst.pk
        assert inst.__str__()
        inst.delete()


class TestExecutionHistoryModel:
    @pytest.mark.django_db(transaction=True)
    def test_model(self, execution_history_1):
        inst = execution_history_1
        assert inst.pk
        assert inst.__str__()

        inst.max_matching = None
        inst.save()
        assert inst.max_matching is None

        inst.delete()
