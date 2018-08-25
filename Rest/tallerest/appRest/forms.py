from django import forms
from appRest import models

class ServicioForm(forms.ModelForm):

    class Meta:
        model=models.Servicio

        fields=[
            'nombre',
            'fecha',
            'direccion',
        ]
        labels={
            'nombre':'Nombre',
            'fecha': 'Fecha'  ,
            'direccion': 'Direccion' ,
        }
        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control'}) ,
            'fecha': forms.DateField(),
            'direccion': forms.Textarea(attrs={'class':'form-control'}),
        }
