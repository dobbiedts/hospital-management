# Generated by Django 3.0.3 on 2020-08-29 11:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0009_auto_20200824_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_Directory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='enter first name', max_length=200)),
                ('last_name', models.CharField(help_text='enter last name', max_length=200)),
                ('age', models.IntegerField(default=None, help_text='Enter doctor age')),
                ('specialty', models.CharField(default=None, max_length=100)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Patient_Directory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique id for this patient', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text="Enter patient's name", max_length=100)),
                ('diagnosis', models.CharField(help_text="Enter patient's diagnosis", max_length=100)),
                ('date', models.DateField(blank=True, null=True)),
                ('summary', models.TextField(help_text='Enter a brief description of the ailment', max_length=1000)),
                ('age', models.IntegerField(default=None, help_text='Enter patients age')),
            ],
        ),
        migrations.DeleteModel(
            name='Assigned_Patient',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='assigned_patient',
        ),
        migrations.RemoveField(
            model_name='instance',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='instance',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='assigned_doctor',
        ),
        migrations.DeleteModel(
            name='Assigned_Doctor',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='Instance',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]