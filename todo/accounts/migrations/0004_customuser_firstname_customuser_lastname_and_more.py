# Generated by Django 4.1.2 on 2022-10-29 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='firstname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='customuser',
            name='lastname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phonenumber',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
