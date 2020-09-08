# Generated by Django 3.0.3 on 2020-08-24 10:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0005_patient_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assigned_Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the assigned doctor', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Assigned_Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the assigned doctor', max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='doctor',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.RenameField(
            model_name='instance',
            old_name='patients',
            new_name='patient',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='patients',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='treatment_course',
        ),
        migrations.RemoveField(
            model_name='instance',
            name='case',
        ),
        migrations.RemoveField(
            model_name='instance',
            name='doctors',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='doctors',
        ),
        migrations.AddField(
            model_name='doctor',
            name='first_name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='doctor',
            name='last_name',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialty',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='instance',
            name='diagnosis',
            field=models.CharField(default=None, help_text='Enter diagnosis for instance', max_length=100),
        ),
        migrations.AlterField(
            model_name='instance',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular case in the hospital', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='instance',
            name='status',
            field=models.CharField(blank=True, choices=[('r', 'receiving treatment'), ('d', 'discharged'), ('a', 'admitted')], default='r', help_text='patient status', max_length=1),
        ),
        migrations.AddField(
            model_name='doctor',
            name='assigned_patient',
            field=models.ManyToManyField(help_text='who is/are the patients assigned to this doctor', to='health.Assigned_Patient'),
        ),
        migrations.AddField(
            model_name='patient',
            name='assigned_doctor',
            field=models.ManyToManyField(help_text='who is/are the doctors assigned to this patient', to='health.Assigned_Doctor'),
        ),
    ]