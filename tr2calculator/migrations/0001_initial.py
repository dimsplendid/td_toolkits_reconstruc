# Generated by Django 3.2.9 on 2022-02-13 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AxomatricsLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Plateform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbr', models.CharField(default='5905', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='OpticsLogTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v90', models.DecimalField(decimal_places=4, max_digits=5)),
                ('v95', models.DecimalField(decimal_places=4, max_digits=5)),
                ('v99', models.DecimalField(decimal_places=4, max_digits=5)),
                ('v100', models.DecimalField(decimal_places=4, max_digits=5)),
                ('vop', models.DecimalField(decimal_places=4, max_digits=5)),
                ('v_percent', models.CharField(choices=[('V90', 'V90'), ('V95', 'V95'), ('V99', 'V99'), ('V100', 'V100'), ('Vref', 'Vref')], max_length=4)),
                ('cell_gap', models.DecimalField(decimal_places=2, max_digits=3)),
                ('lc_percent', models.DecimalField(decimal_places=3, max_digits=6)),
                ('wx', models.DecimalField(decimal_places=9, max_digits=10)),
                ('wy', models.DecimalField(decimal_places=9, max_digits=10)),
                ('u_prime', models.DecimalField(decimal_places=9, max_digits=10)),
                ('v_prime', models.DecimalField(decimal_places=9, max_digits=10)),
                ('delta_uv', models.DecimalField(decimal_places=9, max_digits=10)),
                ('a_star', models.DecimalField(decimal_places=9, max_digits=10)),
                ('b_star', models.DecimalField(decimal_places=9, max_digits=10)),
                ('l_star', models.DecimalField(decimal_places=9, max_digits=10)),
                ('delta_a_star', models.DecimalField(decimal_places=9, max_digits=10)),
                ('delta_b_star', models.DecimalField(decimal_places=9, max_digits=10)),
                ('delta_l_star', models.DecimalField(decimal_places=9, max_digits=10)),
                ('delta_e_ab_star', models.DecimalField(decimal_places=9, max_digits=10)),
                ('contrast_ratio', models.DecimalField(decimal_places=1, max_digits=5)),
                ('delta_contrast_ratio', models.DecimalField(decimal_places=2, max_digits=4)),
                ('transmittance', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('dark_index', models.DecimalField(decimal_places=9, max_digits=10)),
                ('white_index', models.DecimalField(decimal_places=9, max_digits=10)),
                ('time_rise', models.DecimalField(decimal_places=9, max_digits=10)),
                ('time_fall', models.DecimalField(decimal_places=9, max_digits=10)),
                ('response_time', models.DecimalField(decimal_places=9, max_digits=10)),
                ('g2g', models.DecimalField(decimal_places=9, max_digits=10)),
                ('remark', models.CharField(choices=[('Extrapolation', 'Extrapolation'), ('Interpolation', 'Interpolation')], default='Extrapolation', max_length=20)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='tr2calculator.batch')),
                ('liquidCrystal', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='materials.liquidcrystal')),
                ('platform', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tr2calculator.plateform')),
                ('ref_record', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tr2calculator.opticslogtest')),
            ],
        ),
    ]
