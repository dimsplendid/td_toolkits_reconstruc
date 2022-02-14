from django import forms


class TR2ResultUploadForm(forms.Form):
    file = forms.FileField(label="Calculated Sumary excel file")
