# Generated by Django 4.0.4 on 2022-11-01 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_admin_agent_customuser_is_admin_customuser_is_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='agentadmin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agentadmin', to='accounts.admin'),
        ),
    ]
