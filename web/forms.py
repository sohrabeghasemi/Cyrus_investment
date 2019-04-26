from django import forms
from . import models


class kargar_input_form(forms.ModelForm):

	class Meta:
		model = models.kagar_cyrus
		fields = '__all__'