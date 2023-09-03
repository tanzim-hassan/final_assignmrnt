from django.contrib import admin
from .models import category

# Register your models here.
admin.site.register(category)
class categoryAdmin(admin.modelAdmin):
    prepopulated_fields={'slug':('category')}
    list_display=('category','slug')

admin.site.register(category,categoryAdmin)
