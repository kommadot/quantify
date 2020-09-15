from django.contrib import admin

# Register your models here.
from .models import LowVariability, Momentum, RiskMomentum

admin.site.register(LowVariability)
admin.site.register(Momentum)
admin.site.register(RiskMomentum)