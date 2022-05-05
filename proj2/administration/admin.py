from django.contrib import admin
from .models import *

# Register your models here.
all_models = (Member)
admin.site.register(all_models)