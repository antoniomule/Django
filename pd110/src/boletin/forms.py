from django import forms

class RegForm(forms.Form):
	nombre = forms.CharField(required=False)
	edad = forms.IntegerField()