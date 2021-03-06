# Generated by Django 3.0.3 on 2020-08-17 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='patients',
        ),
        migrations.AddField(
            model_name='doctor',
            name='patients',
            field=models.ForeignKey(help_text='patients assigned to the doctor', null=True, on_delete=django.db.models.deletion.SET_NULL, to='health.Patient'),
        ),
        migrations.RemoveField(
            model_name='patient',
            name='doctors',
        ),
        migrations.AddField(
            model_name='patient',
            name='doctors',
            field=models.ForeignKey(help_text='doctor on the case', null=True, on_delete=django.db.models.deletion.SET_NULL, to='health.Doctor'),
        ),
    ]
