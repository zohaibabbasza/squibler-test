# Generated by Django 4.0.2 on 2022-03-01 09:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sections", "0003_section_owner"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="section",
            name="user",
        ),
        migrations.AddField(
            model_name="section",
            name="collaboration",
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
