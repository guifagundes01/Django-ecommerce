from multiprocessing import context
from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Product
from sale.forms import SaleForm
from .forms import ProductForm

class ProductDetailView(DetailView):
  queryset = Product.available.all()
  template_name = "products/product_detail.html"

class ProductListView(ListView):
  def get_queryset(self):
    return Product.available.all()

  def get_context_data(self, **kwargs):
    return super().get_context_data(**kwargs)

  template_name = "products/product_list.html"


class ProductCreate(CreateView):
  model = Product
  form_class = ProductForm
  template_name = "products/product_create_form.html"


class ProductUpdate(UpdateView):
  model = Product
  fields = "__all__"
  template_name = "products/product_update_form.html"

class ProductUpdateList(ListView):
  def get_queryset(self):
    return Product.available.all()

  def get_context_data(self, **kwargs):
    return super().get_context_data(**kwargs)

  template_name = "update_list.html"


