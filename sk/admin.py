from django.contrib import admin
from .models import *

# Register your models here.
myModels = [Clen, Druzstva, Status, Prispevky]
admin.site.register(myModels)
