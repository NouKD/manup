from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Contact)
admin.site.register(models.NewsLetter)
admin.site.register(models.Disposition)