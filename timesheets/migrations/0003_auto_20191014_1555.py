# Generated by Django 2.2.5 on 2019-10-14 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheets', '0002_auto_20191014_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='status',
            field=models.CharField(blank=True, choices=[('blank', ' '), ('Work In Progress', 'Work In Progress'), ('Would Not Be Done', 'Would Not Be Done'), ('To Be Done', 'To Be Done')], default='blank', max_length=20, null=True),
        ),
    ]
