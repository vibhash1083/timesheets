# Generated by Django 2.2.5 on 2019-10-14 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheets', '0005_auto_20191014_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='status',
            field=models.CharField(blank=True, choices=[('WorkInProgress', 'Work In Progress'), ('WouldNotBeDone', 'Would Not Be Done'), ('ToBeDone', 'To Be Done')], max_length=20, null=True),
        ),
    ]
