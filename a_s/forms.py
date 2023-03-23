from django import forms
from .models import AutoSys

class AutoSysForm(forms.ModelForm):
    class Meta:
        model = AutoSys
        fields = ['autosys']

class ASN_IP(forms.Form):
    asn_ip = forms.CharField(label='asn_ip')
