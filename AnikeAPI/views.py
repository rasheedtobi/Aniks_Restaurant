from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage

# Create your views here.
@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method =='GET':
        # item = MenuItem.objects.all()
        item = MenuItem.objects.select_related('category').all() 

        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        page= request.query_params.get('page', default=1)
        perpage= request.query_params.get('perpage', default =2)


        if category_name:
            item = item.filter(category__menu_category = category_name)
        if to_price:
            item = item.filter(price__lte=to_price)
        if search:
            item = item.filter(title__istartswith = search)
        if ordering:
            # item =item.order_by(ordering)
            ordering_fields = ordering.split(',')
            item = item.order_by(*ordering_fields)

        paginator = Paginator(item, per_page=perpage)
        try:
            item = paginator.page(number = page)
        except EmptyPage:
            item = []

        serialized_item = MenuItemSerializer(item, many=True)
        # return Response(items.values()) #without serializers
        return Response(serialized_item.data)
    if request.method =='POST':
        serialized_item = MenuItemSerializer(data = request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)

@api_view()
def single_item(request, id):
    # item = MenuItem.objects.get(pk=id)
    item = get_object_or_404(MenuItem, pk=id)  #To handle errors due to non-existent id
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)