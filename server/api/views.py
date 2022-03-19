from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from .models import Order, Item, Ingredient, Extra

@api_view(['POST', 'GET', 'DELETE'])
def order(request):
    order = Order.get_singleton()
    if request.method == 'POST':
        order.items.add(request.data['id'])
    return Response(order.get_items())

@api_view(['GET'])
def helloworld(request):
    return Response({'message': 'Hello World!'})

@api_view(['POST'])
def sign_up(request):
    user = User.objects.create_user(
        username=request.data['username'], password=request.data['password'])
    return Response()

@api_view(['GET'])
def logout(request):
    request.user.auth_token.delete()
    return Response({'token': None})

@api_view(['GET'])
def menu(request):
    return Response([
        {'name': item.name, 'ingredients': 
            [ingredient.name for ingredient in item.ingredients.all()]
        } 
        for item in Item.objects.all()
    ])