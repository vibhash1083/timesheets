import datetime
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib import messages
class ExcelPageView(TemplateView):
    template_name = "excel_home.html"


import xlwt
import xlrd
from django.http import HttpResponse
from core.models import Task, Role, Member, Category


def export_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="TimeSheet.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    sheets = Role.objects.all()
    mylist =[]
    for sheet in sheets:
        mylist.append(sheet.role_name)
    mysheets=list(dict.fromkeys(mylist))
    # print(mysheets)
    # style = xlwt.XFStyle()
    # pattern = xlwt.Pattern()
    # pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    # pattern.pattern_fore_colour = xlwt.Style.colour_map['dark_purple']
    # style.pattern = pattern

    # fmt = xlwt.Style.easyxf("""
    #     font: name Arial;
    #     borders: left thick, right thick, top thick, bottom thick;
    #     pattern: pattern solid, fore_colour red;
    #     """, num_format_str='YYYY-MM-DD')

    for sheet in mysheets:

        ws = wb.add_sheet(sheet)
        row_num = 0
        # fmt = xlwt.Style.easyxf("""
        #     font: name Calibri;
        #     borders: left thick, right thick, top thick, bottom thick;
        #     pattern: pattern solid, fore_colour black;
        #     height :
        #     """, num_format_str='YYYY-MM-DD')
        font_style1 = xlwt.Style.easyxf('font: name Calibri, bold on, height 180,color black; pattern: pattern solid, fore_colour yellow; border: top_color black, bottom_color black, right_color black, left_color black ;')

        # font_style = xlwt.XFStyle()
        # font_style.font.bold = True

        columns = ['Jira Ticket Type', 'Description', 'Sprints/Releases', 'Team Member', 'Category', 'Hours', 'Week', ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style1)

        # font_style = xlwt.XFStyle()
            font_style2 = xlwt.Style.easyxf('font: name Calibri, height 180; border: top_color black, bottom_color black, right_color black, left_color black;')

    for sheet in sheets:
        # row_num = 0

        ws = wb.get_sheet(sheet.role_name)
        row_num=len(ws._Worksheet__rows)
        # print(row_num)

        rows = Task.objects.filter(role=sheet).values_list('jira_ticket_type', 'description', 'sprint', 'team_name','category','hours','date')
        for row in rows:
            # row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style2)

    wb.save(response)

    return response

def get_current_week(campaign_date):
    formatted_date = datetime.datetime.strptime(
        campaign_date, '%Y-%m-%d').date()
    week_number = formatted_date.isocalendar()[1]
    return week_number


def createpost(request):
    count=0
    role = Role()
    cat = Category()
    mem = Member()
    task = Task()
    check=Task.objects.all()
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
    print(len(check))
    for x in range(len(check)):
        print(x)
        if(check == task):
            count=1

    if(count==0):
        print("saved")
        task.save()

    messages.success(request, 'Details submitted')

    return render(request, 'success.html',
                  {'t': task })

def details(request):
    query = Task.objects.values_list('description',flat=True).distinct()
    return render(request, 'details.html', {'list':query})

def invoke(request):
    return render(request, 'basic.html',{})
