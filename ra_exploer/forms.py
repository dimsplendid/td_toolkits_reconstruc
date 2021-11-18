from django import forms
from django.db.models.query import QuerySet
from .models import LiquidCrystal, Polyimide, Seal


class SearchFrom(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['LC'] = forms.MultipleChoiceField(
        choices=list(LiquidCrystal.objects.all().values_list('name', 'name'))+[('ALL', 'ALL')])
        self.fields['PI'] = forms.MultipleChoiceField(
        choices=list(Polyimide.objects.all().values_list('name', 'name'))+[('ALL', 'ALL')])
        self.fields['Seal'] = forms.MultipleChoiceField(
        choices=list(Seal.objects.all().values_list('name', 'name'))+[('ALL', 'ALL')])

class UploadFileForm(forms.Form):
    file = forms.FileField(required=True, label='File to import')