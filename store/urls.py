from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
    path('add/', views.add_product, name='add_product'),
    path('edit/', views.edit_product, name='edit_product'),
    path('delete/', views.delete_product, name='delete_product'),
]