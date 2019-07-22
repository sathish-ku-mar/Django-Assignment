from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Adult
# Register your models here.
# admin.site.register(Adult)

@admin.register(Adult)
class AdultAdmin(ImportExportModelAdmin):
    pass