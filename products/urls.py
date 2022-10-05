from django.urls import include, path
from .views import ProductCreate, ProductDetailView, ProductListView, ProductUpdate
from sale.views import SaleView, ConfirmSale

app_name = "products"

urlpatterns = [
    path("", ProductListView.as_view(), name="list"),
    path("<slug:slug>/", ProductDetailView.as_view(), name="detail"),
    path("create", ProductCreate.as_view(), name="create"),
    path("update", ProductListView.as_view(), name="update"),
    path("", include("sale.urls", namespace="sale")),
    path("<slug>/update", ProductUpdate.as_view(), name="update"),
]

