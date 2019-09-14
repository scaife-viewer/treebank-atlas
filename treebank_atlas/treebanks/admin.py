from django.contrib import admin

from .models import Treebank, Sentence, Word


@admin.register(Treebank)
class TreebankAdmin(admin.ModelAdmin):
    list_display = ("id", "urn", "name", "metadata")


@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
    list_display = ("id", "treebank", "position")
    raw_id_fields = ("treebank",)


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ("id", "treebank", "sentence", "form", "lemma", "postag", "relation", "head")
    raw_id_fields = ("treebank", "sentence", "head")
