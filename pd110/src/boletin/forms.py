from django import forms

from .models import Registrado

class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["nombre", "email"]

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base, proveeder = email.split("@")
		dominio, extension = proveeder.split(".")
		if not extension == "edu":
			raise forms.ValidationError(" Porfi primo utiliza una extension .edu")
		return email

		def cleam_nomber(self):
			nombre = self.cleaned_data.get("nombre")
			#validaciones
			return nombre

class RegForm(forms.Form):
	nombre = forms.CharField(required=False)
	email = forms.EmailField()