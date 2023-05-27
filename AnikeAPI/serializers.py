from rest_framework import serializers
from .models import MenuItem
from .models import Category
from decimal import Decimal

#One way to write the seraliazer class
# class MenuItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

#Another way to write the class.
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'menu_category']

class MenuItemSerializer(serializers.ModelSerializer):
    stock =serializers.IntegerField(source='inventory') #change attribute name from inventory to stock
    price_after_tax = serializers.SerializerMethodField(method_name = 'tax_calculator')
    # category = serializers.StringRelatedField()
    category = CategorySerializer(read_only = True)
    category_id = serializers.IntegerField(write_only =True)
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock','price_after_tax', 'category', 'category_id']

    def tax_calculator(self, item_price:MenuItem):
        return item_price.price * Decimal(1.1)
    
  
