from django.db import models

class Role(models.Model):
    role_name = models.CharField(max_length=20)

    def __str__(self):
        return self.role_name

class Member(models.Model):
    mem_name = models.CharField(max_length=50)
    team_name = models.CharField(max_length=50)
    def __str__(self):
        return self.mem_name

class Category(models.Model):
    category = models.CharField(max_length=20)
    def __str__(self):
        return self.category


class Task(models.Model):
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    jira_ticket_type = models.CharField(max_length=20)
    jira_ticket_number = models.IntegerField()
    description = models.CharField(max_length=100)
    sprint = models.CharField(max_length=20)
    team_name =models.ForeignKey(Member,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    hours = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.jira_ticket_type

