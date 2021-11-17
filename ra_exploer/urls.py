from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('search'),
    url(r'^export/csv/$', views.export_results_csv, name='export_results_csv'),
    path('import/adhesion', views.import_adhesion, name='import_adhesion'),
    path('import/lowTemperatureOperation', views.import_LTO, name='import_lto'),
    path('import/lowTemperatureStorage', views.import_LTS, name='import_lts'),
    path('import/deltaAngle', views.import_DeltaAngle, name='import_deltaAngle'),
    path('import/vhr', views.import_VHR, name='import_vhr')
]
