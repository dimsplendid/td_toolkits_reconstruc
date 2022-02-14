from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View
from django.views.generic.edit import FormView

import pandas as pd
import plotly.express as px
from plotly.offline import plot

from .forms import TR2ResultUploadForm
from .models import OpticsLogTest, Batch, Plateform
from .models import LiquidCrystal


class HomepageView(TemplateView):
    template_name = 'tr2_calculator_generic.html'


class TR2ResultUploadFormView(FormView):
    template_name = "tr2_calculator_upload.html"
    form_class = TR2ResultUploadForm
    success_url = reverse_lazy('tr2_calculator:results-upload')

    def form_valid(self, form):
        print("Form Success!")
        filename = self.request.FILES['file'].file
        upload_df = pd.read_excel(filename, engine='openpyxl')
        for row in upload_df.to_dict(orient='records'):
            lc, _ = LiquidCrystal.objects.get_or_create(name=row['LC'])
            batch, _ = Batch.objects.get_or_create(value=row['Batch'])
            platform, _ = Plateform.objects.get_or_create(abbr='5905')
            if not OpticsLogTest.objects.filter(
                batch=batch,
                liquidCrystal=lc,
                platform=platform,
                vop=row['Vop(V)'],
                cell_gap=row['Gap(um)'],
            ).exists():
                OpticsLogTest.objects.create(
                    batch=batch,
                    liquidCrystal=lc,
                    v90=row['V90'],
                    v95=row['V95'],
                    v99=row['V99'],
                    v100=row['V100'],
                    vop=row['Vop(V)'],
                    v_percent=row['V%'],
                    platform=platform,
                    cell_gap=row['Gap(um)'],
                    lc_percent=row['LC%'],
                    wx=row['Wx'],
                    wy=row['Wy'],
                    u_prime=row["u'"],
                    v_prime=row["v'"],
                    delta_uv=row["Δ(u', v')"],
                    a_star=row['a*'],
                    b_star=row['b*'],
                    l_star=row['L*'],
                    delta_a_star=row['Δa*'],
                    delta_b_star=row['Δb*'],
                    delta_l_star=row['ΔL*'],
                    delta_e_ab_star=row['ΔEab*'],
                    contrast_ratio=row['CR'],
                    delta_contrast_ratio=row['ΔCR(%)'],
                    transmittance=row['T%'],
                    dark_index=row['D'],
                    white_index=row['W'],
                    time_rise=row['Tr(ms)'],
                    time_fall=row['Tf(ms)'],
                    response_time=row['RT(ms)'],
                    g2g=row['G2G(ms)'],
                    remark=row['remark']
                )
        return super().form_valid(form)


def opt_score(column, cmp='gt'):
    stdev = column.std()
    mean = column.mean()
    score = (column - mean) / stdev
    if cmp == 'lt':
        score = -score
    return score


class TR2OptSearchView(View):
    def get(self, request, *args, **kwargs):
        batch_list = Batch.objects.all()
        q = self.request.GET.get('q')
        div_fig = None
        if q:
            result = OpticsLogTest.objects.filter(
                v_percent='Vref',
                cell_gap=3.0,
                batch__value=q
            )

            opt_result_df = pd.DataFrame.from_records(
                result.values(
                    "liquidCrystal__name",
                    "lc_percent",
                    "delta_e_ab_star",
                    "response_time",
                    "contrast_ratio"
                )
            )

            opt_result_df.columns = [
                'LC',
                'LC%',
                'ΔEab*',
                'RT(ms)',
                'CR',
            ]
            opt_score_df = opt_result_df[['LC']].copy()
            opt_score_df['LC%'] = opt_score(
                opt_result_df['LC%'].astype('float'))
            opt_score_df['ΔEab*'] = opt_score(
                opt_result_df['ΔEab*'].astype('float'), 'lt')
            opt_score_df['RT(ms)'] = opt_score(
                opt_result_df['RT(ms)'].astype('float'), 'lt')
            opt_score_df['CR'] = opt_score(opt_result_df['CR'].astype('float'))

            opt_score_df['sum'] = opt_score_df.sum(axis=1)
            opt_score_df = opt_score_df.sort_values(by='sum', ascending=False)
            plot_df = opt_score_df.set_index('LC').stack().reset_index()
            plot_df.columns = ['LC', 'Item', 'Score']
            opt_fig = px.bar(plot_df, x='LC', y='Score',
                             color='Item', barmode='group')
            div_fig = plot(opt_fig, output_type='div')
            request.session['opt result'] = opt_result_df.to_json()
            request.session['opt score'] = opt_score_df.to_json()
            request.session['filtered LC list'] = opt_score_df[[
                'LC']].to_json()

        return render(
            request,
            'tr2_calculator_query.html',
            context=({
                'batch_list': batch_list,
                'q': q,
                'div_fig': div_fig,
            })
        )


class TR2OptDataDownload(View):
    def get(self, request, *args, **kwargs):
        if request.session['opt result'] and request.session['opt score']:
            opt_result_df = pd.read_json(request.session['opt result'])
            opt_score_df = pd.read_json(request.session['opt score'])
            with BytesIO() as b:
                writer = pd.ExcelWriter(b, engine='openpyxl')
                opt_result_df.to_excel(
                    writer, sheet_name='OPT Result', index=False)
                opt_score_df.to_excel(
                    writer, sheet_name='OPT Score', index=False)
                writer.save()
                filename = 'OptResult.xlsx'
                response = HttpResponse(
                    b.getvalue(),
                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
                response['Content-Disposition'] = f'attachment; filename={filename}'
                return response
