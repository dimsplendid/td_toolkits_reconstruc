from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomepageView.as_view(), name='home'),
    path('results-upload/', views.TR2ResultUploadFormView.as_view(),
         name='results-upload'),
    path('query/', views.TR2OptSearchView.as_view(), name='query'),
    path('query/download/', views.TR2OptDataDownload.as_view(),
         name='query-download'),
]
