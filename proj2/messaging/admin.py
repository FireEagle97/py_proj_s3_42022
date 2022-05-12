from django.contrib import admin
from .models import *
all_models = (Message)
admin.site.register(all_models)
# Register your models here.