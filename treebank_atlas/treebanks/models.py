from django.contrib.postgres.fields import JSONField
from django.db import models


class Treebank(models.Model):
    urn = models.CharField(max_length=255)
    name = models.CharField(blank=True, null=True, max_length=255)
    metadata = JSONField(encoder="", default=dict, blank=True)

    class Meta:
        ordering = ["urn"]

    def __str__(self):
        return self.name


class Sentence(models.Model):

    position = models.IntegerField()
    idx = models.IntegerField(help_text="0-based index")

    treebank = models.ForeignKey(
        "treebanks.Treebank", related_name="sentences", on_delete=models.CASCADE
    )


class Word(models.Model):

    position = models.IntegerField()
    idx = models.IntegerField(help_text="0-based index")

    treebank = models.ForeignKey(
        "treebanks.Treebank", related_name="words", on_delete=models.CASCADE
    )
    sentence = models.ForeignKey(
        "treebanks.Sentence", related_name="words", on_delete=models.CASCADE
    )

    form = models.CharField(max_length=50)
    lemma = models.CharField(max_length=50, null=True, blank=True)
    postag = models.CharField(max_length=9, null=True, blank=True)
    relation = models.CharField(max_length=16)
    head = models.ForeignKey(
        "self",
        related_name="dependants",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
