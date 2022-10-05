from django.urls import path

from .views import HomePageView, ManageProducts

from products.views import ProductCreate, ProductListView, ProductUpdateList


app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("manage", ManageProducts.as_view(), name="manage"),
    path("manage/create", ProductCreate.as_view(), name="create"),
    path("manage/update", ProductUpdateList.as_view(), name="update-list"),

]