
from django.urls import path
from core import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# urlpatterns = [
#
#     path('home', views.invoke, name='invoke'),
#     path('export/excel', views.export_xls, name='export_excel'),
#     path('save', views.createpost, name='save'),
#     path('data', views.details, name='data'),
#
#
# ]


urlpatterns = [

    path('', views.HomeView.as_view(), name='home_view'),
    path('view_report/', views.ReportView.as_view(), name='report_view'),
    path('generate_report/', views.GenerateReport.as_view(), name='generate_report_view'),
    path('fetch_report/', views.FetchReportView.as_view(), name='fetch_report_view'),
    path('export_excel/<date:start_date>', views.export_excel, name='export_excel_view'),


]

urlpatterns += staticfiles_urlpatterns()