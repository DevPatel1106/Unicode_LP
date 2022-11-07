# Generated by Django 4.1.2 on 2022-11-07 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todoapp', '0004_todolist_listagent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='listadmin',
        ),
        migrations.AlterField(
            model_name='todolist',
            name='listagent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listagent', to=settings.AUTH_USER_MODEL),
        ),
    ]
