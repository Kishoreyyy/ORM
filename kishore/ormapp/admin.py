

from django.contrib import admin

# Register your models here.
from .models import bankloan,bankloanAdmin
admin.site.register(bankloan,bankloanAdmin)