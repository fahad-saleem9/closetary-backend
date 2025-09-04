from django.urls import path
from .views import (
    CategoryListCreateView,
    CategoryDetailView,
    SubcategoryListCreateView,
    SubcategoryDetailView,
    WardrobeItemListCreateView,
    WardrobeItemDetailView,
)

urlpatterns = [
    
    path("categories/", CategoryListCreateView.as_view(), name="category-list-create"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),

    
    path("subcategories/", SubcategoryListCreateView.as_view(), name="subcategory-list-create"),
    path("subcategories/<int:pk>/", SubcategoryDetailView.as_view(), name="subcategory-detail"),

    
    path("items/", WardrobeItemListCreateView.as_view(), name="wardrobeitem-list-create"),
    path("items/<int:pk>/", WardrobeItemDetailView.as_view(), name="wardrobeitem-detail"),
]
