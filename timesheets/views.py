import datetime

from django.views.generic.edit import FormView, View
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render

from .forms import WorklogForm, ReportForm
from .models import Task, Worklog


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
        form = ReportForm()
        context = {}
        context['worklog_data'] = worklog_data
        context['form'] = form
        return render(request, 'report.html', context)

    def post(self, request, *args, **kwargs):
        form = ReportForm(request.POST, request.FILES)
        start_date = datetime.date(int(form.data.get('start_date_year')), int(
            form.data.get('start_date_month')), int(form.data.get('start_date_day')))
        end_date = datetime.date(int(form.data.get('end_date_year')), int(
            form.data.get('end_date_month')), int(form.data.get('end_date_day')))
        worklog_data = Worklog.objects.filter(
            work_date__gte=start_date, work_date__lte=end_date)
        context = {}
        context['worklog_data'] = worklog_data
        context['form'] = form
        return render(request, 'report.html', context)


def export_excel(request):
    print("export excel")
    pass
