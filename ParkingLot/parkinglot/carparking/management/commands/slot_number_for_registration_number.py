from django.core.management.base import BaseCommand, CommandError, CommandParser
from carparking.models import Slot, Car
from django.db import IntegrityError


class Command(BaseCommand):
    help = "List all cars slot number with a given registration number in the parking lot"

    def add_arguments(self, parser: CommandParser) -> None:
        "Add cli arguments"
        parser.add_argument('reg_num', type=str)


    def handle(self, *args, **options):
        """Action performed by this command is here"""
        reg_num = options['reg_num']
        try:
            car = Car.objects.get(reg_number = reg_num)
            self.stdout.write(f"{car.slot}")
        except Car.DoesNotExist:
            self.stderr.write(f"Not found!")

        