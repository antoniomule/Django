from django import forms

class RegForm(forms.Form):
	nombre = forms.Charfield(max_Length=100)
	edad = forms.IntegerField()