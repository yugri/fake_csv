from django.contrib import admin
from data_generator.models import Schema, Column, Dataset


class SchemaAdmin(admin.ModelAdmin):
    pass


class ColumnAdmin(admin.ModelAdmin):
    pass


class DatasetAdmin(admin.ModelAdmin):
    pass


admin.site.register(Schema, SchemaAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Dataset, DatasetAdmin)