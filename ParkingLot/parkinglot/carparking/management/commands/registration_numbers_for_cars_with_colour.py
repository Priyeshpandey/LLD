from django.core.management.base import BaseCommand, CommandError, CommandParser
from carparking.models import Slot, Car
from django.db import IntegrityError


class Command(BaseCommand):
    help = "List all cars registartion number with a given colour in the parking lot"

    def add_arguments(self, parser: CommandParser) -> None:
        "Add cli arguments"
        parser.add_argument('colour', type=str)


    def handle(self, *args, **options):
        """Action performed by this command is here"""
        colour = options['colour']
        cars = Car.objects.filter(colour=colour, slot__isnull=False)
        if not cars:
            self.stdout.write("No cars with this color is in our parking lot!")
            return
        for car in cars:
            self.stdout.write(car.reg_number)

        