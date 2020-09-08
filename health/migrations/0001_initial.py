# Generated by Django 3.0.3 on 2020-08-17 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter doctor's name", max_length=100)),
                ('treatment_course', models.TextField(help_text='Enter a brief description of course of treatment', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique id for this patient', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text="Enter patient's name", max_length=100)),
                ('diagnosis', models.CharField(help_text="Enter patient's diagnosis", max_length=100)),
                ('date', models.DateField(blank=True, null=True)),
                ('summary', models.TextField(help_text='Enter a brief description of the ailment', max_length=1000)),
                ('doctors', models.ManyToManyField(help_text='doctor on the case', to='health.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique id for this case', primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, choices=[('p', 'patient receiving treatment'), ('d', 'discharged'), ('a', 'admitted')], default='p', help_text='patient status', max_length=1)),
                ('case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('doctors', models.ManyToManyField(help_text='doctor on the case', to='health.Doctor')),
                ('patients', models.ManyToManyField(help_text='patients assigned to the doctor', to='health.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='patients',
            field=models.ManyToManyField(help_text='patients assigned to the doctor', to='health.Patient'),
        ),
    ]
