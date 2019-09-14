from django.contrib import admin

from .models import Treebank


@admin.register(Treebank)
class TreebankAdmin(admin.ModelAdmin):
    list_display = ("id", "urn", "name", "metadata")
