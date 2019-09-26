import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView, View
from django.urls import reverse_lazy

from .forms import WorklogForm, ReportForm
from .models import Task, Worklog
from .export_excel import generate_excel_report


class HomeView(FormView):
    form_class = WorklogForm
    template_name = 'home.html'
    success_url = reverse_lazy('report_view')

    def form_valid(self, form):
        form.save()
        return super(HomeView, self).form_valid(form)


class ReportView(View):

    def get(self, request, *args, **kwargs):
        worklog_data = Worklog.objects.all()
        start_date = datetime.date(2019, 1, 1)
        end_date = datetime.date(2022, 12, 31)
        form_data = {
            'start_date': start_date,
            'end_date': end_date
        }
        form = ReportForm(form_data)
        context = {}
        context['worklog_data'] = worklog_data
        context['form'] = form
        return render(request, 'report.html', context)

    def post(self, request, *args, **kwargs):
        form = ReportForm(request.POST, request.FILES)
        start_date = datetime.datetime.strptime(form.data.get('start_date'), '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(form.data.get('end_date'), '%Y-%m-%d').date()
        if request.POST:
            if '_submit' in request.POST:
                worklog_data = Worklog.objects.filter(work_date__gte=start_date, work_date__lte=end_date)
                context = {}
                context['worklog_data'] = worklog_data
                context['form'] = form
                return render(request, 'report.html', context)
            elif '_download' in request.POST:
                response = HttpResponse(content_type='application/ms-excel')
                response['Content-Disposition'] = 'attachment; filename="TimeSheet.xls"'
                workbook = generate_excel_report(start_date, end_date)
                workbook.save(response)
                return response
            elif '_add' in request.POST:
                response = redirect('/')
                return response



