# Generated by Django 2.2.5 on 2019-09-24 12:55

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
                ('category', models.CharField(choices=[('Bug', 'bug'), ('Story', 'story'), ('Design', 'design'), ('Development', 'development'), ('PTO', 'PTO')], default='Bug', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mem_name', models.CharField(max_length=50)),
                ('team_name', models.CharField(choices=[('QA-MARINNE', 'qa_marinne'), ('QA-JASON', 'qa_jason'), ('DEV', 'dev'), ('SMILE-CHECK-Support', 'smile_check_support')], default='QA_MARINNE', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jira_ticket_type', models.CharField(max_length=20)),
                ('jira_ticket_number', models.IntegerField(null=True)),
                ('description', models.CharField(max_length=100)),
                ('sprint', models.CharField(max_length=20)),
                ('hours', models.IntegerField()),
                ('date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Team')),
            ],
        ),
    ]
