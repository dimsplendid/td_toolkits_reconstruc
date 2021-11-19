# Generated by Django 3.2.5 on 2021-11-19 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ra_exploer', '0028_vhr'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LowTemperatrueStorage',
            new_name='LowTemperatureStorage',
        ),
        migrations.AddField(
            model_name='liquidcrystal',
            name='vender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='ra_exploer.vender'),
        ),
    ]
