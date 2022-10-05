from multiprocessing import context, get_context
from urllib import request
from webbrowser import get
from django.forms import SlugField
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from django.views import View
from django.views.generic import CreateView, TemplateView
from products.models import Product
from sale.forms import SaleForm


from sale.models import Sale


# Create your views here.

class SaleView(CreateView):
  model = Sale
  form_class = SaleForm
  template_name = "products/product_sale_form.html"

  def get_context_data(self, **kwargs):
    product = get_object_or_404(Product, slug = self.kwargs['slug'])
    print(product)
    context = super().get_context_data(**kwargs)
    context['product'] = product
    return context

  def form_valid(self, form):
    sale = form.save(commit=False)
    product = get_object_or_404(Product, slug = self.kwargs['slug'])
    sale.product_id = product.id
    sale.total_value = product.price * sale.quantity
    sale.save()
    product.stock -= 1
    product.save()
    return HttpResponseRedirect(reverse("products:sale:confirm", kwargs={"slug":self.kwargs['slug'], "sale_id": sale.id}))


class ConfirmSale(TemplateView):
  template_name = "products/sale_confirmed.html"
  def get_context_data(self, **kwargs):
    self.product = get_object_or_404(Product, slug = self.kwargs['slug'])
    self.sale = get_object_or_404(Sale, id = self.kwargs['sale_id'])
    context = super().get_context_data(**kwargs)
    context['sale'] = self.sale
    context['product'] = self.product
    return context



