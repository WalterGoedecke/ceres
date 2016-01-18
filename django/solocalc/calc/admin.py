from django.contrib import admin

# Register your models here.
from mezzanine.core.admin import TabularDynamicInlineAdmin, SingletonAdmin
from mezzanine.pages.admin import PageAdmin

from calc.models import *

admin.site.register(Calculation, CalculationAdmin)