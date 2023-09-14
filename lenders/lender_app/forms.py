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


class UpdateLenderForm(forms.ModelForm):
    class Meta:
        model = Lender
        fields = ('name', 'code', 'upfront_com',
                  'trial_com', 'active')

    def __init__(self, *args, **kwargs):
        # Get the instance of the Lender model using the pk
        instance = Lender.objects.get(id=kwargs.pop('id', 1))
        # Pass the instance to the super class constructor
        super().__init__(instance=instance, *args, **kwargs)
        # Customize the form fields as you wish
        self.fields['name'].widget = forms.TextInput(attrs={'placeholder': instance.name})
        self.fields['code'].widget = forms.TextInput(attrs={'placeholder': instance.code, 'max_length': 3})
        self.fields['upfront_com'].widget = forms.NumberInput(attrs={'placeholder': instance.upfront_com})
        self.fields['trial_com'].widget = forms.NumberInput(attrs={'placeholder': instance.trial_com})
        self.fields['active'].widget = forms.CheckboxInput(attrs={'default': instance.active if instance else ''})

    helper = helper.FormHelper
