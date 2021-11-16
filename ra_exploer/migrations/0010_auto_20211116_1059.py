# Generated by Django 3.2.5 on 2021-11-16 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ra_exploer', '0009_auto_20211116_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adhesion',
            name='judgement',
            field=models.CharField(blank=True, choices=[('NG', 'NG'), ('OK', 'OK')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='adhesion',
            name='peeling',
            field=models.CharField(blank=True, help_text='Enter peeling interface.', max_length=40, null=True),
        ),
    ]