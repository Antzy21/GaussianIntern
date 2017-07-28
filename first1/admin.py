from django.contrib import admin

# Register your models here.
from first1.models import Sankey, Sankey2, Pie1


class Sankey2Admin(admin.ModelAdmin):
    list_display = ['source', 'target', 'value']


class Pie1Admin(admin.ModelAdmin):
    list_display = ['name', 'value']


admin.site.register(Sankey)
admin.site.register(Sankey2, Sankey2Admin)
admin.site.register(Pie1, Pie1Admin)
