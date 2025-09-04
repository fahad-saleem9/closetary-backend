from rest_framework import serializers
from .models import Category, Subcategory, WardrobeItem  

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class SubcategorySerializer(serializers.ModelSerializer): 
    class Meta:
        model = Subcategory
        fields = "__all__"

class WardrobeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardrobeItem
        fields = "__all__"
