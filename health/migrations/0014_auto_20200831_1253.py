# Generated by Django 3.0.3 on 2020-08-31 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('health', '0013_auto_20200831_1146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assigned_doctor',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AlterModelOptions(
            name='instance',
            options={'ordering': ['date'], 'permissions': (('can_mark_admitted', 'Set patient as admitted'), ('can_mark_as_discharegd', 'Set Patient as discharged'))},
        ),
        migrations.AddField(
            model_name='instance',
            name='operator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]