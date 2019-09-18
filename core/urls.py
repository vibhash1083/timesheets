  
from django.urls import path
from core import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('home',views.invoke,name='invoke'),
    path('export/excel', views.export_xls, name='export_excel'),
    path('save', views.createpost, name='save'),
    path('data', views.details, name='data'),


]


urlpatterns += staticfiles_urlpatterns()