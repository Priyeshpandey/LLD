from django.contrib import admin
from carparking.models import Car, Command, Slot


# Register your models here.
admin.site.register(Command)
admin.site.register(Car)
admin.site.register(Slot)
