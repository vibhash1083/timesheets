
from django.urls import path
from timesheets import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.HomeView.as_view(), name='home_view'),
    path('view_report/', views.ReportView.as_view(), name='report_view'),
]

urlpatterns += staticfiles_urlpatterns()