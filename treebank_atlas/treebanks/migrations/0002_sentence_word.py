# Generated by Django 2.2.5 on 2019-09-14 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("treebanks", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Sentence",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position", models.IntegerField()),
                ("idx", models.IntegerField(help_text="0-based index")),
                (
                    "treebank",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sentences",
                        to="treebanks.Treebank",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Word",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position", models.IntegerField()),
                ("idx", models.IntegerField(help_text="0-based index")),
                ("form", models.CharField(max_length=50)),
                ("lemma", models.CharField(max_length=50)),
                ("postag", models.CharField(max_length=9)),
                ("relation", models.CharField(max_length=8)),
                (
                    "head",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="dependants",
                        to="treebanks.Word",
                    ),
                ),
                (
                    "sentence",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="words",
                        to="treebanks.Sentence",
                    ),
                ),
                (
                    "treebank",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="words",
                        to="treebanks.Treebank",
                    ),
                ),
            ],
        ),
    ]
