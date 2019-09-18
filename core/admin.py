from django.contrib import admin
from .models import Role, Task, Member, Category
# Register your models here.
admin.site.register(Role)
admin.site.register(Task)
admin.site.register(Member)
admin.site.register(Category)