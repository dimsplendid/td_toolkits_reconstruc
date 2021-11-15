from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('search'),
    url(r'^export/csv/$', views.export_results_csv, name='export_results_csv')
]
