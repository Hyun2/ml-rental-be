# Generated by Django 2.2.7 on 2019-11-08 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20191108_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='birth_month',
            field=models.CharField(max_length=50, verbose_name='BIRTH MONTH'),
        ),
        migrations.AlterField(
            model_name='member',
            name='birth_year',
            field=models.CharField(max_length=50, verbose_name='BIRTH YEAR'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='contract_period',
            field=models.CharField(max_length=50, verbose_name='CONTRACT PERIOD'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='num_arrear',
            field=models.CharField(max_length=50, verbose_name='NUMBER OF ARREAR'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='rental_cost',
            field=models.CharField(max_length=50, verbose_name='RENTAL COST'),
        ),
    ]
