from django.forms import ModelForm
from . import models

class ingresoIp(ModelForm):
    class Meta:
        model = models.ingresoIp
        fields =['ip']
