from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# Adds this to the admin page
admin.site.register(Question)
admin.site.register(Choice)