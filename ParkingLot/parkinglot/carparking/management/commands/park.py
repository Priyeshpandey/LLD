from django.core.management.base import BaseCommand, CommandError
from carparking.models import Slot, Car
from django.db import IntegrityError


class Command(BaseCommand):
    help = "Parks a car with given registration \
        number and color to an available slot if it exists"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('reg_number', type=str)
        parser.add_argument('colour', type=str)

    def handle(self, *args, **options):
        """Action performed by this command is here"""
        car_reg_number = options['reg_number']
        colour = options['colour']

        # check for an empty slot
        s = Slot.objects.filter(car__isnull=True).first()
        if not s:
            self.stderr.write("No Empty Slots available!")
        else:
            car, created = Car.objects.get_or_create(reg_number=car_reg_number,
                                        colour=colour)
            if car.slot:
                self.stdout.write(f"{car} is already parked!")
            else:
                car.slot = s
                car.save()
                self.stdout.write(f"{car} is parked in slot {s}")
        