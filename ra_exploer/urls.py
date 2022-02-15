from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('search'),
    url(r'^export/csv/$', views.export_results_csv, name='export_results_csv'),
    path('import/adhesion/', views.import_adhesion, name='import_adhesion'),
    path('import/lowTemperatureOperation/',
         views.import_LTO, name='import_lto'),
    path('import/lowTemperatureStorage/', views.import_LTS, name='import_lts'),
    path('import/deltaAngle/', views.import_DeltaAngle, name='import_deltaAngle'),
    path('import/vhr/', views.import_VHR, name='import_vhr'),
    path('import/pct/', views.import_PCT, name='import_pct'),
    path('import/sealwvtr/', views.import_SealWVTR, name='import_sealwvtr'),
    path('validator/<str:slug>/update/',
         views.ValidatorUpdateView.as_view(), name='valid-update'),
    path('query/filteredResult/', views.filteredResultView, name='filtered-result'),
    path('query/filteredResult/download/',
         views.xlsx_export, name='filtered-result-download'),
    path('test/', views.test, name='test'),
    path('test/download/', views.test_download, name='test-download'),
    path('create/batch', views.BatchUploadView.as_view(), name='ra-batch-upload')
]
