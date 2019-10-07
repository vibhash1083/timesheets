import xlsxwriter
from math import ceil
from .models import *

def get_current_week(date):
    first_day = date.replace(day=1)
    dom = date.day
    adjusted_dom = dom + first_day.weekday()

    return int(ceil(adjusted_dom / 7.0))

def add_sheets(sheets,workbook):
    for sheet in sheets:
        worksheet = workbook.add_worksheet(sheet.group_name)
        cell_format1 = workbook.add_format({'bold': True, 'font_name': 'Times New Roman'})
        cell_format1.set_bg_color('yellow')
        titles = [
            'Jira Ticket Type',
            'Jira Ticket Number',
            'Description',
            'Sprints/Releases',
            'Team Member',
            'Category',
            'Hours',
            'Week',
        ]
        row_number = 0
        for column_number in range(len(titles)):
            worksheet.write(row_number, column_number, titles[column_number], cell_format1)

def add_data(sheets, workbook, from_date, to_date, team_member):
    cell_format2 = workbook.add_format({'font_name': 'Times New Roman'})
    for sheet in sheets:
        worksheet = workbook.get_worksheet_by_name(sheet.group_name)
        row_number = 1
        if team_member is None:
            rows = Worklog.objects.filter(work_date__gte=from_date, work_date__lte=to_date,
                                          member__group_name__group_name__contains=sheet.group_name)
        else:
            rows = Worklog.objects.filter(work_date__gte=from_date, work_date__lte=to_date,
                                      member__group_name__group_name__contains=sheet.group_name, member__name__contains=team_member)
        for row in rows:
            worksheet.write(row_number, 0, row.task.jira_ticket_type.ticket_type, cell_format2)
            worksheet.write(row_number, 1, row.task.jira_ticket_number, cell_format2)
            worksheet.write(row_number, 2, row.task.description, cell_format2)
            worksheet.write(row_number, 3, row.task.sprint, cell_format2)
            worksheet.write(row_number, 4, row.member.name, cell_format2)
            worksheet.write(row_number, 5, row.task.category.category_name, cell_format2)
            worksheet.write(row_number, 6, row.hours, cell_format2)
            worksheet.write(row_number, 7, "Week-" + get_current_week(row.work_date).__str__(), cell_format2)
            row_number += 1


def add_statistics(sheets, workbook, from_date, to_date):
    cell_format1 = workbook.add_format({'bold': True, 'font_name': 'Times New Roman'})
    cell_format1.set_bg_color('yellow')
    cell_format2 = workbook.add_format({'font_name': 'Times New Roman'})
    for sheet in sheets:
        worksheet = workbook.get_worksheet_by_name(sheet.group_name)
        worksheet.write(1, 9, "Team Member", cell_format1)
        worksheet.write(1, 10, "Sum of Hours", cell_format1)
        member_names = Member.objects.filter(
            group_name__group_name__contains=sheet.group_name)
        names_list = []
        hours_list = []
        for member_name in member_names:
            if member_name.name not in names_list:
                names_list.append(member_name.name)
        total_sum_of_hours = 0
        number_of_members = len(names_list)
        for i in range(number_of_members):
            work_logs = Worklog.objects.filter(
                member__name__contains=names_list[i],
                work_date__gte=from_date,
                work_date__lte=to_date)
            worksheet.write(i + 2, 9, names_list[i], cell_format2)
            sum_of_hours = 0
            for work_log in work_logs:
                sum_of_hours += work_log.hours
            hours_list.append(sum_of_hours)
            worksheet.write(i + 2, 10, sum_of_hours, cell_format2)
            total_sum_of_hours += sum_of_hours
        names_list.append("Total")
        hours_list.append(total_sum_of_hours)
        worksheet.write(number_of_members + 2, 9, "Total", cell_format1)
        worksheet.write(number_of_members + 2, 10, total_sum_of_hours, cell_format1)

        pie_chart = workbook.add_chart({'type': 'pie'})
        pie_chart.set_title({'name': 'Statistics'})
        pie_chart.set_style(10)
        pie_chart.add_series({'categories':[sheet.group_name, 2, 9, 2+len(names_list)-1, 9],
                              'values':[sheet.group_name, 2, 10, 2+len(names_list)-1, 10],
                              'data_labels': {'value': False, 'percentage':True, 'category': False, 'position': 'outside_end'}
                              })
        worksheet.insert_chart('M2', pie_chart, {'x_offset': 25, 'y_offset': 10})


def generate_excel_report(from_date, to_date, team_member):
    workbook = xlsxwriter.Workbook('Timesheets.xlsx')
    sheets = Group.objects.all()
    add_sheets(sheets, workbook)
    add_data(sheets, workbook, from_date, to_date, team_member)
    if team_member is not None:
        add_statistics(sheets, workbook, from_date, to_date)

    workbook.close()
