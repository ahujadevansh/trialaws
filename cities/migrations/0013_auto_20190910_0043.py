# Generated by Django 2.2.4 on 2019-09-09 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0012_auto_20190910_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='ideal_duration',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='city',
            name='region',
            field=models.CharField(choices=[('North India', 'North India'), ('South India', 'South India'), ('East India', 'East India'), ('West India', 'West India'), ('Central India', 'Central India'), ('North-East', 'North-East'), ('International', 'International')], max_length=500),
        ),
    ]