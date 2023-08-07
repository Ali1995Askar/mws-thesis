import argparse
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from management.selectors import ManagementSelectors


def validate_density(arg):
    MIN_VAL = 0
    MAX_VAL = 1

    try:
        value = float(arg)
    except ValueError:
        raise argparse.ArgumentTypeError("Must be a able to parse to float")

    if value < MIN_VAL or value > MAX_VAL:
        raise argparse.ArgumentTypeError("Argument must be < " + str(MAX_VAL) + " and > " + str(MIN_VAL))
    return value


def validate_nodes_number(arg):
    MIN_VAL = 2
    MAX_VAL = 1000

    try:
        value = int(arg)
    except ValueError:
        raise argparse.ArgumentTypeError("Must be a able to parse to int")

    if value < MIN_VAL or value > MAX_VAL:
        raise argparse.ArgumentTypeError("Argument must be < " + str(MAX_VAL) + " and > " + str(MIN_VAL))
    return value


class Command(BaseCommand):
    help = 'Fill DB SCRIPT'

    def add_arguments(self, parser):
        parser.add_argument(
            '-n',
            '--nodes',
            type=validate_nodes_number,
            default=100
        )

        parser.add_argument(
            '-d',
            '--density',
            type=validate_density,
            default=1
        )

        parser.add_argument(
            '-u',
            '--username',
            type=str,
            choices=list(User.objects.all().values_list('username', flat=True)),

        )

    def handle(self, *args, **options):
        density = options.get('density')
        nodes = options.get('nodes')
        username = options.get('username')
        kwargs = {'nodes': nodes, 'density': density}

        if username:
            kwargs['username'] = username

        ManagementSelectors.random_build_graph(**kwargs)
