from django.urls import path
from .views import MyOrderView, CreateOrderProductsView


urlpatterns = [
    path("mi-orden", MyOrderView.as_view(), name="my_order"),
    path("agregar-producto", CreateOrderProductsView.as_view(), name="add_product"),
]
