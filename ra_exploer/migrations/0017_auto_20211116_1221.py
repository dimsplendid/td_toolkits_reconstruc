# Generated by Django 3.2.5 on 2021-11-16 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ra_exploer', '0016_alter_acis_device'),
    ]

    operations = [
        migrations.AddField(
            model_name='lowtemperatrueoperation',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='ra_exploer.vendor'),
        ),
        migrations.AddField(
            model_name='lowtemperatruestorage',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='ra_exploer.vendor'),
        ),
    ]