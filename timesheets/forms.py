from django import forms
from django.forms import Textarea
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class WorklogForm(forms.Form):
    member_name = forms.ModelChoiceField(queryset=Member.objects.all())
    team_name = forms.ModelChoiceField(queryset=Team.objects.all())
    task_category = forms.ModelChoiceField(queryset=TaskCategory.objects.all())
    ticket_type = forms.ModelChoiceField(queryset=TicketType.objects.all(), initial="ENG")
    ticket_number = forms.IntegerField(required=False)
    ticket_description = forms.CharField()
    sprint = forms.CharField(label='Release Version', required=False)
    worked_date = forms.DateField(
        label='Date',
        widget = DateInput,
        initial=datetime.date.today)
    hours_worked = forms.IntegerField(label='Hours Worked', initial=8)

    def save(self, id=None):
        if id:
            worklog = Worklog.objects.get(pk=id)
            worklog.member.name = self.cleaned_data.get('member_name')
            worklog.member.team_name = self.cleaned_data.get('team_name')
            worklog.task.category.category_name = self.cleaned_data.get(
                'task_category')
            worklog.task.jira_ticket_type.ticket_type = self.cleaned_data.get(
                'ticket_type')
            worklog.task.jira_ticket_number = self.cleaned_data.get(
                'ticket_number')
            worklog.task.description = self.cleaned_data.get(
                'ticket_description')
            worklog.task.sprint = self.cleaned_data.get('sprint')
            worklog.hours = self.cleaned_data.get('hours_worked')
            worklog.work_date = self.cleaned_data.get('worked_date')
            worklog.save()

        else:
            task_category = self.cleaned_data.get('task_category')
            jira_ticket_type = self.cleaned_data.get('ticket_type')
            jira_ticket_number = self.cleaned_data.get('ticket_number')
            description = self.cleaned_data.get('ticket_description')
            sprint = self.cleaned_data.get('sprint')
            task_entry = Task(category=task_category,
                              jira_ticket_type=jira_ticket_type,
                              jira_ticket_number=jira_ticket_number,
                              description=description,
                              sprint=sprint)
            task_entry.save()

            member = self.cleaned_data.get('member_name')
            worked_date = self.cleaned_data.get('worked_date')
            worked_hours = self.cleaned_data.get('hours_worked')

            worklog_entry = Worklog(task=task_entry,
                                    member=member,
                                    work_date=worked_date,
                                    hours=worked_hours)

            worklog_entry.save()


class ReportForm(forms.Form):
    start_date = forms.DateField(label='Start Date', widget=DateInput)
    end_date = forms.DateField(label='End Date', widget=DateInput)
    team_member = forms.ModelChoiceField(label='Member Name', required=False, queryset=Member.objects.all())

class FeedbackForm(forms.ModelForm):
    
    class Meta:
        model = Feedback
        fields = [
            'name',
            'feedback',
            'status'
        ]
        widgets = {
            'feedback': Textarea(attrs={'cols': 40, 'rows': 10}),
        }

