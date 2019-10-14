from django.db import models

import datetime


class Team(models.Model):
    team_name = models.CharField(max_length=20)

    def __str__(self):
        return self.team_name


class Group(models.Model):
    group_name = models.CharField(max_length=20)

    def __str__(self):
        return self.group_name


class Member(models.Model):
    name = models.CharField(max_length=50)
    group_name = models.ForeignKey(Group, on_delete=models.CASCADE)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TaskCategory(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name


class TicketType(models.Model):
    ticket_type = models.CharField(max_length=5)

    def __str__(self):
        return self.ticket_type


class Task(models.Model):
    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE)
    jira_ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    jira_ticket_number = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=100)
    sprint = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.jira_ticket_type.ticket_type + \
            '-' + str(self.jira_ticket_number)


class Worklog(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    work_date = models.DateField(default=datetime.date.today)
    hours = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False, verbose_name="Is Deleted")

    def delete(self, *args, **kwargs):
        if self.is_deleted:
            return
        self.is_deleted = True
        self.save()

    def __str__(self):
        return self.member.name

class Feedback(models.Model):
    name = models.ForeignKey(Member, on_delete=models.CASCADE)
    feedback = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ("WorkInProgress", "Work In Progress"),
        ("WouldNotBeDone", "Would Not Be Done"),
        ("ToBeDone", "To Be Done")
    ]
    status = models.CharField(max_length=20, choices=status_choices, default=' ', null=True, blank=True)
    

    def __str__(self):
        return self.name.name
