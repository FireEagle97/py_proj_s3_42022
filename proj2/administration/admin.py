from django.contrib import admin

from administration.models import *

all_models = (Member, Member_Warn)
admin.site.register(all_models)
# Register your models here.
