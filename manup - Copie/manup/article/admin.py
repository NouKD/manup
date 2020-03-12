from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.presentation)
admin.site.register(models.Programme)
admin.site.register(models.Tag)
admin.site.register(models.Article)
