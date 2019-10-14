# Generated by Django 2.2.5 on 2019-10-14 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timesheets', '0003_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timesheets.Member'),
        ),
    ]
