from attr import field
from django.views.generic.edit import UpdateView
from django.urls import reverse

from .models import LiquidCrystal


class LCUpdateCellGapView(UpdateView):
    template_name = "lc_update_cell_gap.html"
    template_name_suffix = 'update'
    model = LiquidCrystal
    slug_field = 'name'
    fields = ['designed_cell_gap']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_url'] = self.request.GET.get('next')
        return context

    def get_success_url(self) -> str:
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse('tr2_calculator:query')