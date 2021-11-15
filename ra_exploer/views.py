from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic import TemplateView
from django.http import HttpResponse
from itertools import chain
import csv

# Create your views here.

from .models import LiquidCrystal, Polyimide, Seal, Vendor, TemplateItem, VHR, DeltaAngle, Adhesion
from .forms import SearchFrom


class index(TemplateView):
    template_name = 'index.html'


def index(request):
    """View function for home page of site."""

    query = {
        'LC': [x[0] for x in LiquidCrystal.objects.all().values_list('name')],
        'PI': [x[0] for x in Polyimide.objects.all().values_list('name')],
        'Seal': [x[0] for x in Seal.objects.all().values_list('name')],
    }

    LCs = LiquidCrystal.objects.all()
    PIs = Polyimide.objects.all()
    seals = Seal.objects.all()

    if request.method == 'POST':
        form = SearchFrom(request.POST)
        if form.is_valid():
            query = {
                'LC': form.cleaned_data['LC'],
                'PI': form.cleaned_data['PI'],
                'Seal': form.cleaned_data['Seal'],
            }
            # return HttpResponseRedirect(reverse('export_results_csv'))
            return render(request, 'index.html', context=({'form': form, 'query': query, 'LCs': LCs, 'PIs': PIs, 'seals': seals}))

    else:
        form = SearchFrom
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=({'form': form, 'query': query, 'LCs': LCs, 'PIs': PIs, 'seals': seals}))


def query_table(query, model, writer):
    results = model.objects.all()
    print(query)
    if 'ALL' in query['LC']:
        if 'ALL' in query['PI']:
            if 'ALL' in query['Seal']:
                results = model.objects.all()
            else:
                results = model.objects.filter(
                    seal__name__in=query['Seal'])
        elif 'ALL' in query['Seal']:
            results = model.objects.filter(
                PI__name__in=query['PI'])
        else:
            results = model.objects.filter(
                PI__name__in=query['PI'], seal__name__in=query['Seal'])
    elif 'ALL' in query['PI']:
        if 'ALL' in query['LC']:
            results = model.objects.filter(
                seal__name__in=query['Seal'])
        elif 'ALL' in query['Seal']:
            results = model.objects.filter(
                LC__name__in=query['LC'])
        else:
            results = model.objects.filter(
                LC__name__in=query['LC'], seal__name__in=query['Seal'])
    elif 'ALL' in query['Seal']:
        if 'ALL' in query['PI']:
            results = model.objects.filter(
                LC__name__in=query['LC'])
        elif 'ALL' in query['LC']:
            results = model.objects.filter(
                PI__name__in=query['PI'])
        else:
            results = model.objects.filter(
                PI__name__in=query['PI'], LC__name__in=query['LC'])
    else:
        results = model.objects.filter(
            LC__name__in=query['LC'], PI__name__in=query['PI'], seal__name__in=query['Seal'])

    for result in results:

        row = ['', '', '', '', '', '', '', '']
        if not(result.name is None):
            row[0] = result.name
        if not(result.LC is None):
            row[1] = result.LC.name
        if not(result.PI is None):
            row[2] = result.PI.name
        if not(result.seal is None):
            row[3] = result.seal.name
        if not(result.cond is None):
            row[4] = result.cond()
        if not(result.value is None):
            row[5] = result.value
        if not(result.vendor is None):
            row[6] = result.vendor.name
        if not(result.file_source is None):
            row[7] = result.file_source

        writer.writerow(row)
    print('query finished')


def export_results_csv(request):
    if request.method == 'POST':
        form = SearchFrom(request.POST)
        if form.is_valid():
            query = {
                'LC': form.cleaned_data['LC'],
                'PI': form.cleaned_data['PI'],
                'Seal': form.cleaned_data['Seal'],
            }
            response = HttpResponse(content_type='text/csv; charset=utf-8')
            response['Content-Disposition'] = 'attachment; filename="results.csv"'
            writer = csv.writer(response)
            writer.writerow(['Item', 'LC', 'PI', 'Seal',
                             'Condition', 'Value', 'Vendor', 'file'])

            # need fixed?
            query_table(query, VHR, writer)
            query_table(query, DeltaAngle, writer)
            query_table(query, Adhesion, writer)

            return response
