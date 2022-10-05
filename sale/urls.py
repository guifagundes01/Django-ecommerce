from django.urls import path
from .views import ConfirmSale, SaleView

app_name = "sales"

urlpatterns = [
    path("sale", SaleView.as_view(), name="sale"),
    path("<slug:slug>/sale",SaleView.as_view(), name="sale_order"),
    path("<slug:slug>/sale/<int:sale_id>", ConfirmSale.as_view(), name="confirm"),
    
]