# Generated by Django 2.0.7 on 2018-11-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_auto_20181003_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='term',
            field=models.CharField(max_length=100),
        ),
    ]
