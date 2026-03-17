
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='products'),
    path('cart/', views.cart_view, name='cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove'),
    path('update/<int:item_id>/<str:action>/', views.update_quantity, name='update'),
]
