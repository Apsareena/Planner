from django.contrib import admin
from .models import Todo, Diary

# Register your models here.
admin.site.register(Todo)
admin.site.register(Diary)