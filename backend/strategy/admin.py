from django.contrib import admin

# Register your models here.
from .models import LowVariability, Momentum, RiskMomentum, Value, Quality

admin.site.register(LowVariability)
admin.site.register(Momentum)
admin.site.register(RiskMomentum)
admin.site.register(Value)
admin.site.register(Quality)