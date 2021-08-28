from django.contrib import admin
from catalog import models


admin.site.register(models.Pet)
admin.site.register(models.Dog)
admin.site.register(models.Breed)

