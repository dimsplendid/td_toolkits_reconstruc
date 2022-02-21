from django.urls import path
from . import views

app_name = 'materials'
urlpatterns = [
    path(
        '<str:slug>/update-cell-gap', 
        views.LCUpdateCellGapView.as_view(),
        name='update_lc_designed_cell_gap'
    )
]