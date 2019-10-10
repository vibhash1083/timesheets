
from django.urls import path
from timesheets import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.HomeView.as_view(), name='home_view'),
    path('view_report/', views.ReportView.as_view(), name='report_view'),
    path('edit/<worklog_id>/', views.EditView.as_view(), name='edit_view'),
    path('delete/<worklog_id>', views.DeleteView.as_view(), name='delete_view')

]

urlpatterns += staticfiles_urlpatterns()