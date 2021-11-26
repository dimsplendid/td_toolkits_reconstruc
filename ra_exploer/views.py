from django.views.generic.edit import UpdateView
from django.forms.models import model_to_dict
from django.http.response import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views.generic import TemplateView
from django.http import HttpResponse
from itertools import chain
import csv
from openpyxl.reader.excel import load_workbook

# Create your views here.

from .forms import SearchFrom, UploadFileForm
from .models import VHR, DeltaAngle, LiquidCrystal, LowTemperatureOperation, Polyimide, Seal, Validator, Vender, File
from .models import Adhesion, LowTemperatureStorage


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

    form = SearchFrom
    file_form = UploadFileForm
    valid_adhesion = Validator.objects.get(name='adhesion test')
    valid_LTO = Validator.objects.get(name='LTO')
    valid_LTS = Validator.objects.get(name='LTS')
    valid_delta_angle = Validator.objects.get(name='Δ angle')
    valid_VHR = Validator.objects.get(name='VHR(heat)')

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context=(
            {
                'form': form,
                'query': query,
                'LCs': LCs,
                'PIs': PIs,
                'seals': seals,
                'file_form': file_form,
                'valid_adhesion': valid_adhesion,
                'valid_LTO': valid_LTO,
                'valid_LTS': valid_LTS,
                'valid_delta_angle': valid_delta_angle,
                'valid_VHR': valid_VHR,
            }
        )
    )


def import_adhesion(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            # print('valid!')
            ws = load_workbook(
                filename=request.FILES['file'].file).worksheets[0]
            header = True  # using for skip header, it should have a nicer method?

            for row in ws.values:
                if header:
                    header = False
                    continue
                lc, _ = LiquidCrystal.objects.get_or_create(name=row[1])
                pi, _ = Polyimide.objects.get_or_create(name=row[2])
                seal, _ = Seal.objects.get_or_create(name=row[3])
                vender, _ = Vender.objects.get_or_create(name=row[8])
                file, _ = File.objects.get_or_create(name=row[9])
                if not Adhesion.objects.filter(LC=lc, PI=pi, seal=seal, vender=vender, file_source=file,
                                               adhesion_interface=row[5], method=row[6]).exists():
                    Adhesion.objects.create(LC=lc, PI=pi, seal=seal, vender=vender, file_source=file,
                                            adhesion_interface=row[5], method=row[6], value=row[4], peeling=row[7])
            return redirect(reverse('index'))

        else:
            return HttpResponseBadRequest()
    return redirect(reverse('index'))


def import_LTO(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            print('valid!')
            ws = load_workbook(
                filename=request.FILES['file'].file).worksheets[0]

            header = True  # using for skip header, it should have a nicer method?
            for row in ws.values:
                if header:
                    header = False
                    continue
                LC, _ = LiquidCrystal.objects.get_or_create(name=row[1])
                PI, _ = Polyimide.objects.get_or_create(name=row[2])
                seal, _ = Seal.objects.get_or_create(name=row[3])
                vender, _ = Vender.objects.get_or_create(name=row[9])
                file, _ = File.objects.get_or_create(name=row[10])
                JarTestSeal, _ = Seal.objects.get_or_create(name=row[7])
                if not LowTemperatureOperation.objects.filter(LC=LC, PI=PI, seal=seal, vender=vender, file_source=file,
                                                              storage_condition=row[5], SLV_condition=row[6],
                                                              JarTestSeal=JarTestSeal,
                                                              measure_temperature=row[8]).exists():

                    LowTemperatureOperation.objects.create(LC=LC, PI=PI, seal=seal, vender=vender, file_source=file,
                                                           storage_condition=row[5], SLV_condition=row[6],
                                                           JarTestSeal=JarTestSeal, measure_temperature=row[8],
                                                           value=LowTemperatureOperation.value_mapping[row[4]])
            return redirect(reverse('index'))

        else:
            return HttpResponseBadRequest()
    return redirect(reverse('index'))


def import_LTS(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            print('valid!')
            ws = load_workbook(
                filename=request.FILES['file'].file).worksheets[0]

            header = True  # using for skip header, it should have a nicer method?
            for row in ws.values:
                if header:
                    header = False
                    continue
                LC, _ = LiquidCrystal.objects.get_or_create(name=row[1])
                PI, _ = Polyimide.objects.get_or_create(name=row[2])
                seal, _ = Seal.objects.get_or_create(name=row[3])
                vender, _ = Vender.objects.get_or_create(name=row[9])
                file, _ = File.objects.get_or_create(name=row[10])
                JarTestSeal, _ = Seal.objects.get_or_create(name=row[7])
                if not LowTemperatureStorage.objects.filter(LC=LC, PI=PI, seal=seal, vender=vender, file_source=file,
                                                            storage_condition=row[5], SLV_condition=row[6],
                                                            JarTestSeal=JarTestSeal,
                                                            measure_temperature=row[8]).exists():
                    LowTemperatureStorage.objects.create(LC=LC, PI=PI, seal=seal, vender=vender, file_source=file,
                                                         storage_condition=row[5], SLV_condition=row[6],
                                                         JarTestSeal=JarTestSeal, measure_temperature=row[8],
                                                         value=row[4])
            return redirect(reverse('index'))

        else:
            return HttpResponseBadRequest()
    return redirect(reverse('index'))


def import_DeltaAngle(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            print('valid!')
            ws = load_workbook(
                filename=request.FILES['file'].file).worksheets[0]

            header = True  # using for skip header, it should have a nicer method?
            for row in ws.values:
                if header:
                    header = False
                    continue
                LC, _ = LiquidCrystal.objects.get_or_create(name=row[1])
                PI, _ = Polyimide.objects.get_or_create(name=row[2])
                seal, _ = Seal.objects.get_or_create(name=row[3])
                vender, _ = Vender.objects.get_or_create(name=row[9])
                file, _ = File.objects.get_or_create(name=row[10])
                if not DeltaAngle.objects.filter(LC=LC, PI=PI, seal=seal, vender=vender, file_source=file,
                                                 measure_voltage=row[5], measure_freq=row[6], measure_time=row[7],
                                                 measure_temperature=row[8]).exists():
                    DeltaAngle.objects.create(value=row[4], LC=LC, PI=PI, seal=seal, vender=vender, file_source=file,
                                              measure_voltage=row[5], measure_freq=row[6], measure_time=row[7],
                                              measure_temperature=row[8])
            return redirect(reverse('index'))

        else:
            return HttpResponseBadRequest()
    return redirect(reverse('index'))


def import_VHR(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            print('valid!')
            ws = load_workbook(
                filename=request.FILES['file'].file).worksheets[0]

            header = True  # using for skip header, it should have a nicer method?
            for row in ws.values:
                if header:
                    header = False
                    continue
                LC, _ = LiquidCrystal.objects.get_or_create(name=row[1])
                PI, _ = Polyimide.objects.get_or_create(name=row[2])
                seal, _ = Seal.objects.get_or_create(name=row[3])
                vender, _ = Vender.objects.get_or_create(name=row[9])
                file, _ = File.objects.get_or_create(name=row[10])
                if not VHR.objects.filter(LC=LC, PI=PI, seal=seal, vender=vender, file_source=file,
                                          measure_voltage=row[5], measure_freq=row[6], measure_temperature=row[7],
                                          UV_aging=row[8]).exists():
                    VHR.objects.create(value=row[4], LC=LC, PI=PI, seal=seal, vender=vender, file_source=file,
                                       measure_voltage=row[5], measure_freq=row[6], measure_temperature=row[7],
                                       UV_aging=row[8])
            return redirect(reverse('index'))

        else:
            return HttpResponseBadRequest()
    return redirect(reverse('index'))


def query_table(query, model, writer, valid=True, cmp='gt'):

    valid_val = Validator.objects.get_or_create(name=model.name)[0].value

    if 'ALL' in query['LC']:
        query['LC'] = LiquidCrystal.objects.all().values_list('name')
    if 'ALL' in query['PI']:
        query['PI'] = Polyimide.objects.all().values_list('name')
    if 'ALL' in query['Seal']:
        query['Seal'] = Seal.objects.all().values_list('name')
    if cmp == 'gt':
        results = model.objects.filter(
            LC__name__in=query['LC'],
            PI__name__in=query['PI'],
            seal__name__in=query['Seal'],
            value__gt=valid_val,
        )
    elif cmp == 'lt':
        results = model.objects.filter(
            LC__name__in=query['LC'],
            PI__name__in=query['PI'],
            seal__name__in=query['Seal'],
            value__lt=valid_val,
        )

    for result in results:

        row = ['N.A.'] * 10
        if not (result.name is None):
            row[0] = result.name
        if not (result.LC is None):
            row[1] = result.LC.name
        if not (result.PI is None):
            row[2] = result.PI.name
        if not (result.seal is None):
            row[3] = result.seal.name
        if not (result.value is None):
            if model.name == 'LTO':
                value = result.get_value_display()
            else:
                value = result.value
            row[4] = value
        if not (result.unit is None):
            row[5] = result.unit
        if not (result.value_remark is None):
            row[6] = result.value_remark()
        if not (result.vender is None):
            row[7] = result.vender.name
        if not (result.cond is None):
            row[8] = result.cond()
        if not (result.file_source is None):
            row[9] = result.file_source.name

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
            response = HttpResponse(content_type='text/csv; charset=utf-8-sig')
            response['Content-Disposition'] = 'attachment; filename="results.csv"'
            writer = csv.writer(response)
            writer.writerow(['Item', 'LC', 'PI', 'Seal',
                             'Value', 'Unit', 'Value Remark', 'Vendor', 'Condition', 'file'])

            # need fixed?
            query_table(query, VHR, writer)
            query_table(query, DeltaAngle, writer, cmp='lt')
            query_table(query, Adhesion, writer)
            query_table(query, LowTemperatureOperation, writer)
            query_table(query, LowTemperatureStorage, writer)
            # query_table(query, AC_IS, writer)

            return response
    return redirect(reverse('index'))


class ValidatorUpdateView(UpdateView):
    template_name = 'validator_update.html'
    template_name_suffix = 'update'
    model = Validator
    slug_field = 'name'
    fields = ['value']

    def get_success_url(self):
        return reverse('index')

from plotly.offline import plot
import plotly.graph_objects as go

def test(request):
    x_data = [0, 1, 2, 3]
    y_data = [x**2 for x in x_data]
    plot_div = plot(
        [go.Scatter(
            x=x_data, y=y_data,
            mode='lines',
            name='test',
            opacity=0.8,
            marker_color='green'
        )],
        output_type='div'
    )
    return render(request, 'test.html', context={'plot_div': plot_div})
