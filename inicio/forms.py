from django.forms import ModelForm
from .models import Compra

class InicioForm(ModelForm):
    class Meta:
        model = Compra
        fields = ['title', 'description', 'important']