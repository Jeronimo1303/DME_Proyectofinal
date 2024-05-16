from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Empresa

admin.site.register(Empresa)
