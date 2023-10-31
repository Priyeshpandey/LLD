from django.core.management.base import BaseCommand, CommandError
from carparking.models import Slot, Car
from django.db import IntegrityError


class Command(BaseCommand):
    help = "Shows current status of parking lot"

    def handle(self, *args, **options):
        """Action performed by this command is here"""
        self.stdout.write('Slot Number, Car Registration Number, Colour')
        for slot in Slot.objects.all():
            car = slot.car if hasattr(slot, 'car') else None
            reg_num = car.reg_number if car else '-'
            colour = car.colour if car else '-'
            self.stdout.write(f"{slot.number}, {reg_num}, {colour}")
        