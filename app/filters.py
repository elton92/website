import django_filters
from django_filters import CharFilter
from django import forms

from .models import *

class PosFilter(django_filters.FilterSet):
	titulo = CharFilter(field_name='titulo', lookup_expr="icontains", label='Titulo')
	temas = django_filters.ModelMultipleChoiceFilter(queryset=Tema.objects.all(),
		widget=forms.CheckboxSelectMultiple
		)
	class Meta:
		model = Publicar
		fields = ['titulo', 'temas']