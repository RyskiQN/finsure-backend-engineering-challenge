from django import forms
from crispy_forms import helper, layout
from .models import Lender


class CreateLenderForm(forms.ModelForm):
    class Meta:
        model = Lender
        fields = ('name', 'code', 'upfront_com',
                'trial_com', 'active')
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    code = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'ID'}), max_length=3)
    upfront_com = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': '%'}))
    trial_com = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': '%'}))
    active = forms.BooleanField(widget=forms.CheckboxInput())
    helper = helper.FormHelper
