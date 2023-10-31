from django.core.management.base import BaseCommand, CommandError
from carparking.models import Slot, Car
from django.db import IntegrityError


class Command(BaseCommand):
    help = "Exits a car with given slot number"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('slot', type=str)

    def handle(self, *args, **options):
        """Action performed by this command is here"""
        slot_number = options['slot']

        # check for an empty slot
        try:
            slot = Slot.objects.get(number=slot_number)
        except Slot.DoesNotExist:
            self.stderr.write("This slot does not exists!")
            return
        if hasattr(slot, 'car'):
            car = slot.car
            car.slot = None
            car.save()
            self.stdout.write(f"Car {car} has left the parking, slot {slot}")
        else:
            self.stdout.write(f"This slot is already empty!")
        