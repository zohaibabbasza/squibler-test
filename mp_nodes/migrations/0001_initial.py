# Generated by Django 4.0.2 on 2022-03-01 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TreeSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('collaboration', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mp_owner', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subsection', to='mp_nodes.treesection')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
