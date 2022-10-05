from django import forms
from .models import Sale
from products.models import Product


class SaleForm(forms.ModelForm):
  class Meta:
    model = Sale

    fields = [
      "name",
      "email",
      "cpf",
      "address",
      "quantity",
    ]

    


  
