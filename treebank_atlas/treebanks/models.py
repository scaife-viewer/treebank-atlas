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
