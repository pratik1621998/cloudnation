# Generated by Django 5.0.1 on 2024-02-03 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_userappdetails_database_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userappdetails',
            name='environment_variables',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.environmentvariable'),
        ),
    ]
