from django.urls import path
from products_scripts.views import product_search, product_click_and_redirect, render_home

app_name = 'products_scripts'

urlpatterns = [
    path('', render_home, name='render_home'),
    path('results/', product_click_and_redirect, name='results'),
    path('search', product_search, name='search')
]