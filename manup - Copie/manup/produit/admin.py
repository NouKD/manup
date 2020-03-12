from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Temoignage)
admin.site.register(models.sponsor)
admin.site.register(models.SiteInfo)