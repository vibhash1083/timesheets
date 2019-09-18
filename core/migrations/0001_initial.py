# Generated by Django 2.2.5 on 2019-09-17 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mem_name', models.CharField(max_length=50)),
                ('team_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jira_ticket_type', models.CharField(max_length=20)),
                ('jira_ticket_number', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('sprint', models.CharField(max_length=20)),
                ('hours', models.IntegerField()),
                ('date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Role')),
                ('team_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Member')),
            ],
        ),
    ]
