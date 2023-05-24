from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
@api_view()
def menu_items(request):
    item = MenuItem.objects.all()
    # return Response(items.values())
    serialized_item = MenuItemSerializer(item, many=True)
    return Response(serialized_item.data)

@api_view()
def single_item(request, id):
    # item = MenuItem.objects.get(pk=id)
    item = get_object_or_404(MenuItem, pk=id)  #To handle errors due to non-existent id
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)