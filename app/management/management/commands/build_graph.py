from django.core.management.base import BaseCommand

from management.selectors import ExecutionHistorySelectors


class Command(BaseCommand):
    help = 'Fill DB SCRIPT'

    def add_arguments(self, parser):
        parser.add_argument(
            '-d',
            '--density',
            type=float,
            default=1
        )

        parser.add_argument(
            '-u',
            '--username',
            type=str,

        )

    def handle(self, *args, **options):
        density = options.get('density')
        username = options.get('username')
        kwargs = {'density': density}

        if username:
            kwargs['username'] = username

        ExecutionHistorySelectors.build_random_graph_by_density(**kwargs)
