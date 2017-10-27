from django import forms
from django.forms import ModelForm

class PlanDataForm(forms.Form):

    setback_area = forms.CharField(
        label="SetBack Area(In sq.ft)",
        widget=forms.TextInput(attrs={'size': '50'}),
    )