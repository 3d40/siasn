from django import forms


class FormNIp(forms.Form):
    nip = forms.CharField(label="Masukan Nip", max_length=18)