from django.contrib import admin
from .models import Message

# Register Message models to django admin.
admin.site.register(Message)