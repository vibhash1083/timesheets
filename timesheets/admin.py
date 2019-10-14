from django.contrib import admin
from .models import Team, Task, TaskCategory, TicketType, Member, Worklog, Group, Feedback


# Register your models here.
admin.site.register(Team)
admin.site.register(Group)
admin.site.register(Task)
admin.site.register(TicketType)
admin.site.register(Member)
admin.site.register(TaskCategory)
admin.site.register(Worklog)
admin.site.register(Feedback)
