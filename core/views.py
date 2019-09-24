from math import ceil
from django.shortcuts import render
from django.contrib import messages
import xlwt
from django.http import HttpResponse
from core.models import Task, Role, Member, Category

# Creating an excel sheet
def export_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="TimeSheet.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    sheets = Role.objects.all()
    mylist =[]
    for sheet in sheets:
        mylist.append(sheet.role_name)
    mysheets=list(dict.fromkeys(mylist))

    # Creating sheets in excel with the name of role
    for sheet in mysheets:

        ws = wb.add_sheet(sheet)
        row_num = 0

        font_style1 = xlwt.Style.easyxf('font: name Calibri, bold on, height 180,color black; pattern: pattern solid, fore_colour yellow; border: top_color black, bottom_color black, right_color black, left_color black ;')
        columns = ['Jira Ticket Type','Jira Ticket Number', 'Description', 'Sprints/Releases', 'Team Member', 'Category','Team Name', 'Hours', 'Week', ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style1)
            font_style2 = xlwt.Style.easyxf('font: name Calibri, height 180; border: top_color black, bottom_color black, right_color black, left_color black;')

    # Adding data to sheets
    for sheet in sheets:
        ws = wb.get_sheet(sheet.role_name)
        row_num=len(ws._Worksheet__rows)
        rows = Task.objects.filter(role=sheet).values_list('jira_ticket_type','jira_ticket_number', 'description', 'sprint', 'team_name','category','hours','date')
        for row in rows:
            for col_num in range(len(row)):
                if col_num == 5:
                    get_id = row[col_num]
                    category = Category.objects.get(id=get_id)
                    ws.write(row_num, col_num, category.category, font_style2)
                elif col_num == 4:
                    get_id = row[col_num]
                    member = Member.objects.get(id=get_id)
                    ws.write(row_num, col_num, member.mem_name, font_style2)
                elif col_num == 6:
                    get_id = row[4]
                    member = Member.objects.get(id=get_id)
                    ws.write(row_num, col_num, member.team_name, font_style2)
                elif col_num == 7:
                    ws.write(row_num, col_num, row[col_num-1], font_style2)
                    ws.write(row_num, col_num+1, "Week "+get_current_week(row[col_num]).__str__(), font_style2)
                    ws.write(row_num, col_num+1, "Week "+get_current_week(row[col_num]).__str__(), font_style2)
                else:
                    ws.write(row_num, col_num, row[col_num], font_style2)
    wb.save(response)

    return response

# Converting date to week number of month
def get_current_week(dt):
    first_day = dt.replace(day=1)
    dom = dt.day
    adjusted_dom = dom + first_day.weekday()

    return int(ceil(adjusted_dom / 7.0))

# Fetch data from forms to DB
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
