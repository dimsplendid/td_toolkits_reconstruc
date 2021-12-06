# Generated by Django 3.2.5 on 2021-12-06 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ra_exploer', '0005_auto_20211206_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='SealWVTR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('meashure_condition_1', models.CharField(help_text='measure condition', max_length=40)),
                ('meashure_condition_2', models.CharField(help_text='measure condition', max_length=40)),
                ('LC', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='ra_exploer.liquidcrystal')),
                ('PI', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='ra_exploer.polyimide')),
                ('file_source', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='ra_exploer.file')),
                ('seal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='ra_exploer.seal')),
                ('vender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='ra_exploer.vender')),
            ],
        ),
    ]