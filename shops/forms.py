from django import forms

class LocationForm(forms.Form):
    latitude = forms.FloatField()
    longitude = forms.FloatField()
    srid = forms.IntegerField(widget=forms.HiddenInput(attrs={'value': 4326}))