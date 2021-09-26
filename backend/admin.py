from django.contrib import admin
from .models import Tgbot, Command

# Register your models here.
admin.site.register(Tgbot)
admin.site.register(Command)