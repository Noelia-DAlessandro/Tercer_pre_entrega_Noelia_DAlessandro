from django import forms

from .models import Home


class HomeForm (forms.ModelForm):
    class Meta: 
        model = Home
        fields = ['nombre','apellido', 'nacimiento', 'pais_orige_id']
        