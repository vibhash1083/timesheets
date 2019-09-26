import xlwt
from math import ceil
from .models import *

# Function to genrate week number
def get_current_week(date):
    first_day = date.replace(day=1)
    dom = date.day
    adjusted_dom = dom + first_day.weekday()

    return int(ceil(adjusted_dom / 7.0))

# Function to generate sheets with header in Excel
def get_sheet(sheets, work_book):

    for sheet in sheets:
        write_sheet = work_book.add_sheet(sheet.group_name)
        row_num = 0

        # Adding style to header and other cells of excel
        font_style1 = xlwt.Style.easyxf(
            'font: name Calibri, bold on, height 180,color black; pattern: pattern solid, fore_colour yellow; border: top_color black, bottom_color black, right_color black, left_color black ;')

        columns = ['Jira Ticket Type', 'Jira Ticket Number', 'Description', 'Sprints/Releases',
                   'Team Member', 'Category', 'Hours', 'Week', ]
        # Adding titles into the sheets
        for col_num in range(len(columns)):
            write_sheet.write(row_num, col_num, columns[col_num], font_style1)

# Function to enter the data into excel
def enter_data(sheets, from_date, to_date, work_book):
    for sheet in sheets:
        write_sheet = work_book.get_sheet(sheet.group_name)
        row_num = len(write_sheet._Worksheet__rows)
        rows = Worklog.objects.filter(work_date__gte=from_date, work_date__lte=to_date,
                                      member__group_name__group_name__contains=sheet.group_name)
        font_style1 = xlwt.Style.easyxf(
            'font: name Calibri, bold on, height 180,color black; pattern: pattern solid, fore_colour yellow; border: top_color black, bottom_color black, right_color black, left_color black ;')

        font_style2 = xlwt.Style.easyxf(
            'font: name Calibri, height 180; border: top_color black, bottom_color black, right_color black, left_color black;')

        for row in rows:
            write_sheet.write(row_num, 0, row.task.jira_ticket_type.ticket_type, font_style2)
            write_sheet.write(row_num, 1, row.task.jira_ticket_number, font_style2)
            write_sheet.write(row_num, 2, row.task.description, font_style2)
            write_sheet.write(row_num, 3, row.task.sprint, font_style2)
            write_sheet.write(row_num, 4, row.member.name, font_style2)
            write_sheet.write(row_num, 5, row.task.category.category_name, font_style2)
            write_sheet.write(row_num, 6, row.hours, font_style2)
            write_sheet.write(row_num, 7, "Week-" + get_current_week(row.work_date).__str__(), font_style2)
            row_num += 1
        write_sheet.write(1, 9, "Team Member", font_style1)
        write_sheet.write(1, 10, "Sum of Hours", font_style1)

        member_names = Member.objects.filter(group_name__group_name__contains=sheet.group_name)

        # Removing Duplications
        mylist = []
        for member_name in member_names:
            if member_name.name not in mylist:
                mylist.append(member_name.name)

        # Individual Work hours of team members
        total_sum_of_hours = 0
        number_of_members = len(mylist)
        for i in range(number_of_members):
            work_logs = Worklog.objects.filter(member__name__contains=mylist[i], work_date__gte=from_date,
                                               work_date__lte=to_date)
            write_sheet.write(i + 2, 9, mylist[i], font_style2)
            sum_of_hours = 0
            for work_log in work_logs:
                sum_of_hours += work_log.hours
            write_sheet.write(i + 2, 10, sum_of_hours, font_style2)
            total_sum_of_hours += sum_of_hours

        write_sheet.write(number_of_members + 2, 9, "Total", font_style1)
        write_sheet.write(number_of_members + 2, 10, total_sum_of_hours, font_style1)


def generate_excel_report(from_date, to_date):
    work_book = xlwt.Workbook(encoding='utf-8')
    sheets = Group.objects.all()
    get_sheet(sheets, work_book)
    enter_data(sheets, from_date, to_date, work_book)

    return work_book

