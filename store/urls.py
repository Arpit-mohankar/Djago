from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('product/', views.product_list, name='index'),
    path('product_detail/', views.product_detail, name='index'),
    path('product/', views.product_list, name='product_list'),
    path('signup/', views.signup, name='signup'),
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('update-cart/<int:pk>/', views.update_cart, name='update_cart'),
    path('remove-from-cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('my-orders/', views.my_orders, name='my_orders'),

]
