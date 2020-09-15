# Generated by Django 2.2.6 on 2020-09-15 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LowVariability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('variability', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Momentum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('momentum', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RiskMomentum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('risk_momentum', models.FloatField()),
            ],
        ),
    ]
