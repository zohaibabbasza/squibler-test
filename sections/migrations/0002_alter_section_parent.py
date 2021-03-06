# Generated by Django 4.0.2 on 2022-02-28 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("sections", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="section",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="subsection",
                to="sections.section",
            ),
        ),
    ]
