from django.contrib import admin
from .models import Address, Schedule, Point, Money

# Register your models here.
admin.site.register(Address)
admin.site.register(Schedule)
admin.site.register(Point)
admin.site.register(Money)