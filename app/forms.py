from django import forms
from django.forms import ModelForm

from .models import Publicar

class PostForm(ModelForm):

	class Meta:
		model = Publicar
		fields = '__all__'

		widgets = {
			'temas':forms.CheckboxSelectMultiple(),
		}