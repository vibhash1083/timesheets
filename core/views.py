import datetime
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib import messages
class ExcelPageView(TemplateView):
    template_name = "excel_home.html"


import xlwt
from django.http import HttpResponse
from core.models import Task, Role, Member, Category


def export_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="TimeSheet.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    sheets = Role.objects.all()

    for sheet in sheets:
        ws = wb.add_sheet(sheet.role_name)
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Jira Ticket', 'Description', 'Sprints/Releases', 'Team Member', 'Category', 'Hours', 'Week', ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

    for sheet in sheets:
        row_num = 0
        ws = wb.get_sheet(sheet.role_name)
        rows = Task.objects.filter(role=sheet).values_list('jira_ticket', 'description', 'sprint', 'team_member','category','hours','week')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

def get_current_week(campaign_date):
    formatted_date = datetime.datetime.strptime(
        campaign_date, '%Y-%m-%d').date()
    week_number = formatted_date.isocalendar()[1]
    return week_number


def createpost(request):

    role = Role()
    cat = Category()
    mem = Member()
    task = Task()

    role.role_name = request.POST.get('role_name')
    mem.mem_name = request.POST.get('mem_name')
    mem.team_name = request.POST.get('team_name')
    cat.category = request.POST.get('category')
    role.save()
    mem.save()
    cat.save()
    task.jira_ticket_type = request.POST.get('jira_ticket_type')
    task.jira_ticket_number = request.POST.get('jira_ticket_number')
    task.description = request.POST.get('description')
    task.sprint = request.POST.get('sprint')
    task.hours = request.POST.get('hours')
    task.date = request.POST.get('date')
    task.category = cat
    task.team_name = mem
    task.role = role
    task.save()

    messages.success(request, 'Details submitted')

    return render(request, 'success.html',
                  {'t': task })

def details(request):
    query = Task.objects.all()
    return render(request, 'details.html', {'list':query})

def invoke(request):
    return render(request, 'basic.html',{})
