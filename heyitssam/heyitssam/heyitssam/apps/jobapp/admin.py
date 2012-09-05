from django.contrib import admin
from models import *

class JobAppAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('company_name',)}
    list_display = ('position', 'company_name', 'visible',)
    list_editable = ('visible',)

admin.site.register(JobApp, JobAppAdmin)
