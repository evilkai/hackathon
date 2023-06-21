from django.contrib import admin

# Register your models here.

from .models import Student, Ad, Telegram

admin.site.register(Student)
admin.site.register(Ad)
admin.site.register(Telegram)