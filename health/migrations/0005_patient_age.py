# Generated by Django 3.0.3 on 2020-08-17 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0004_auto_20200817_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.IntegerField(default=None, help_text='Enter patients age'),
        ),
    ]
