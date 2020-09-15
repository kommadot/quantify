from django.contrib import admin
from .models import Simulation,SimulationBreakdown
# Register your models here.
@admin.register(Simulation)
@admin.register(SimulationBreakdown)
class SimulationAdmin(admin.ModelAdmin):
    pass