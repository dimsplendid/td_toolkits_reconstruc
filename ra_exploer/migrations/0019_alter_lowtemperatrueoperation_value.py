# Generated by Django 3.2.5 on 2021-11-16 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ra_exploer', '0018_alter_lowtemperatrueoperation_storage_condtion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lowtemperatrueoperation',
            name='value',
            field=models.CharField(choices=[('OK', 'OK'), ('NG', 'NG')], max_length=10, null=True),
        ),
    ]
