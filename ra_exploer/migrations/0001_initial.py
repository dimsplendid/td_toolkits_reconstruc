# Generated by Django 3.2.9 on 2021-11-14 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LiquidCrystal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a LC name', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Polyimide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a PI name', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Seal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a Seal name', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Vendor name', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TemplateItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_source', models.CharField(help_text='file name', max_length=200)),
                ('value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('LC', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='ra_exploer.liquidcrystal')),
                ('PI', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='ra_exploer.polyimide')),
                ('seal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='ra_exploer.seal')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='ra_exploer.vendor')),
            ],
        ),
    ]