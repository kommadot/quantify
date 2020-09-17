# Generated by Django 2.2.6 on 2020-09-17 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20)),
                ('social_id', models.CharField(max_length=30)),
                ('platform', models.CharField(max_length=10)),
                ('budget', models.FloatField(default=10000000)),
            ],
        ),
    ]
