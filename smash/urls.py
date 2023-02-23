from django.urls import path
from . import views
urlpatterns = [
    path('products_category/', views.ProductsCategoryViews.as_view()),
    path('products/', views.ProductsViews.as_view()),
    path('product/', views.ProductViews.as_view()),
]