from django.db import models


class Car(models.Model):
    reg_number = models.CharField(max_length=40, primary_key=True)
    colour = models.CharField(max_length=10)
    slot = models.OneToOneField('Slot', on_delete=models.SET_NULL, null=True, related_name='car')

    def __str__(self) -> str:
        return f'{self.reg_number} | {self.colour}'

class Slot(models.Model):
    number = models.PositiveIntegerField(primary_key=True)

    def __str__(self) -> str:
        return f'{self.number}'

class Command(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name



