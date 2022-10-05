from tkinter import CASCADE
from django.db import models
from django.urls import reverse
from products.models import Product


# Create your models here.

class Sale(models.Model):
  name = models.CharField("Nome Completo", max_length=200)
  email = models.EmailField(max_length=200)
  cpf = models.CharField(max_length=30)
  address = models.CharField("Endereço", max_length=250)
  date = models.DateField(auto_now_add=True)
  product_id = models.IntegerField(null=True)
  quantity = models.PositiveIntegerField("Quantidade")
  total_value = models.DecimalField(max_digits=7, decimal_places=2, null=True)

  def __str__(self):
    return str(self.id)

  class Meta:
    ordering = ['-date']

  def get_absolute_url(self):
    return reverse("sale:confirmed", kwargs={"sale_id": self.id})

    

  


  
