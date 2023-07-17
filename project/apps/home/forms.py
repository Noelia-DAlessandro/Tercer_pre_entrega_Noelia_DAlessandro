from django import forms

from .models import Usuario


class HomeForm (forms.ModelForm):
    class Meta: 
        model = Usuario
        fields = ['nombre','apellido', 'nacimiento', 'pais_origen_id']
        