# Generated by Django 2.2.5 on 2019-10-14 09:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('group_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timesheets.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jira_ticket_number', models.CharField(default=' ', max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('sprint', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Worklog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_date', models.DateField(default=datetime.date.today)),
                ('hours', models.IntegerField(default=0)),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timesheets.Member')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timesheets.Task')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timesheets.TaskCategory'),
        ),
        migrations.AddField(
            model_name='task',
            name='jira_ticket_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timesheets.TicketType'),
        ),
        migrations.AddField(
            model_name='member',
            name='team_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timesheets.Team'),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(blank=True, choices=[('blank', ' '), ('WorkInProgress', 'Work In Progress'), ('WouldNotBeDone', 'Would Not Be Done'), ('ToBeDone', 'To Be Done')], default='blank', max_length=20, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timesheets.Member')),
            ],
        ),
    ]
