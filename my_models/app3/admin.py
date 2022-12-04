from django.contrib import admin
from app3.models import Topping
from app3.models import Pizza

# Register your models here.
admin.site.register(Topping)
admin.site.register(Pizza)
