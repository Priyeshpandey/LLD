from django.core.management.base import BaseCommand, CommandError
from carparking.models import Slot
from django.db import IntegrityError


class Command(BaseCommand):
    help = "Creates a parking lot of given size"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("size", type=int)

    def handle(self, *args, **options):
        """Action performed by this command is here"""
        size = options['size']

        # creating `size` slots for parking lot.
        for i in range(1, size+1):
            try:
                s = Slot.objects.create(number=i)
                self.stdout.write(f'Created slot number {i}')
            except IntegrityError:
                self.stderr.write(f"Slot with number {i} already exists")
                continue
        self.stdout.write(f"Created a parking lot with {size} slots")