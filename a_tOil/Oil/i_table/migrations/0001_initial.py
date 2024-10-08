# Generated by Django 5.1 on 2024-08-31 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='infotable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=5)),
                ('yaer', models.IntegerField()),
                ('maker', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=50)),
                ('e_vehicle_type', models.CharField(max_length=50)),
                ('e_range', models.IntegerField()),
                ('legislative_district', models.IntegerField()),
                ('electric_utility', models.CharField(max_length=100)),
            ],
        ),
    ]
