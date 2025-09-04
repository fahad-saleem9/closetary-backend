from rest_framework import generics
from .models import Category, Subcategory, WardrobeItem  
from .serializers import CategorySerializer, SubcategorySerializer, WardrobeItemSerializer  

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubcategoryListCreateView(generics.ListCreateAPIView):  
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

class SubcategoryDetailView(generics.RetrieveUpdateDestroyAPIView):  
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

class WardrobeItemListCreateView(generics.ListCreateAPIView):
    queryset = WardrobeItem.objects.all()
    serializer_class = WardrobeItemSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  

class WardrobeItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WardrobeItem.objects.all()
    serializer_class = WardrobeItemSerializer
