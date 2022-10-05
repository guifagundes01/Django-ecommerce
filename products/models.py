from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse

# Create your models here.

class ProductManager(models.Manager):
  def get_queryset(self):
    return super().get_queryset().exclude(stock=False)

class Product(models.Model):
  name = models.CharField("Nome", max_length=200)
  slug = AutoSlugField(unique=True, always_update=True, populate_from="name")
  img = models.ImageField("Imagem", upload_to='media/images/', blank=True)
  price = models.DecimalField("Preço", decimal_places=2, max_digits=7)
  stock = models.IntegerField("Estoque")
  in_stock = models.BooleanField("Em estoque", default=True)

  products = models.Manager()
  available = ProductManager()

  class Meta:
    ordering = ('name',)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("products:detail", kwargs={"slug": self.slug})
    



