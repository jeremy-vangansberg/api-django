from django import forms
from django import forms
from . import models


class ApiForm(forms.ModelForm):
    class Meta:
        model = models.ApiModel
        fields = "__all__"
        labels = {
            "slug": "Entrez votre cryptomonnaie ici",
            "convert": "Entre votre devise ici"
        }
