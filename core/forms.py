from django import forms

from .models import *


class WorklogForm(forms.Form):
    member_name = forms.ModelChoiceField(queryset = Member.objects.all() )
    team_name = forms.ModelChoiceField(queryset = Team.objects.all() )
    task_category = forms.ModelChoiceField(queryset = TaskCategory.objects.all())
    ticket_type = forms.ModelChoiceField(queryset = TicketType.objects.all())
    ticket_number = forms.IntegerField()
    ticket_description = forms.CharField()
    sprint = forms.CharField(required=False)
    worked_date =  forms.DateField(label='Date', widget=forms.SelectDateWidget)
    hours_worked = forms.IntegerField(label='Hours Worked')

    def save(self):
        # import ipdb; ipdb.set_trace()
        task_category = self.cleaned_data.get('task_category')
        jira_ticket_type = self.cleaned_data.get('ticket_type')
        jira_ticket_number = self.cleaned_data.get('ticket_number')
        description = self.cleaned_data.get('ticket_description')
        sprint = self.cleaned_data.get('sprint')

        # import ipdb; ipdb.set_trace()
        task_entry = Task(category = task_category,
                          jira_ticket_type = jira_ticket_type,
                          jira_ticket_number = jira_ticket_number,
                          description = description,
                          sprint = sprint)
        task_entry.save()

        member = self.cleaned_data.get('member_name')
        worked_date = self.cleaned_data.get('worked_date')
        worked_hours = self.cleaned_data.get('hours_worked')

        worklog_entry = Worklog(task = task_entry,
                                member = member,
                                work_date = worked_date,
                                hours = worked_hours)

        worklog_entry.save()


class ReportForm(forms.Form):
    start_date = forms.DateField(label='Date', widget=forms.SelectDateWidget)
    end_date = forms.DateField(label='Date', widget=forms.SelectDateWidget)
