# Generated by Django 3.2.7 on 2021-09-25 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0002_truck_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='IFTA_group',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='truck',
            name='leave_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='truck',
            name='percentage',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='truck',
            name='rate_per_hour',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='truck',
            name='rate_per_mile_EMPTY',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='truck',
            name='rate_per_mile_LOAD',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='truck',
            name='tour',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='truck',
            name='value',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='truck',
            name='weight_pounds',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='truck',
            name='year',
            field=models.IntegerField(blank=True),
        ),
    ]