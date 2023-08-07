import pytest
from django.core.management import call_command, CommandError


class TestBuildGraphCommand:
    @pytest.mark.django_db(transaction=True)
    def test_call_user_name_arg(self, svu_user, mocker):
        selector_mock = mocker.patch('management.selectors.ManagementSelectors.build_graph')
        call_command('build_graph', '-u', svu_user.username)
        selector_mock.assert_called_once_with(nodes=100, density=1, username=svu_user.username)

    @pytest.mark.django_db(transaction=True)
    def test_call_density_arg(self, svu_user, mocker):
        selector_mock = mocker.patch('management.selectors.ManagementSelectors.build_graph')
        call_command('build_graph', '-d', 0.3)
        selector_mock.assert_called_once_with(nodes=100, density=0.3)

    @pytest.mark.django_db(transaction=True)
    def test_call_nodes_arg(self, svu_user, mocker):
        selector_mock = mocker.patch('management.selectors.ManagementSelectors.build_graph')
        call_command('build_graph', '-n', 500)
        selector_mock.assert_called_once_with(nodes=500, density=1)

    @pytest.mark.django_db(transaction=True)
    def test_wrong_values(self, svu_user, mocker):
        mocker.patch('management.selectors.ManagementSelectors.build_graph')

        with pytest.raises(CommandError) as ere:
            call_command('build_graph', '-u', 'un-exists')

        with pytest.raises(CommandError) as ere:
            call_command('build_graph', '-d', 1.3)
            call_command('build_graph', '-d', -1)

        with pytest.raises(CommandError) as ere:
            call_command('build_graph', '-n', 1)
            call_command('build_graph', '-n', 1001)
