from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response

from reference.models import Product
from store.models import ShoppingCart, Order, OrderItem
from store.serializers import ShoppingCartSerializer, OrderSerializer


# Client specific ViewSet to Add, Update Shopping Cart for registered Users
class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    http_method_names = ['get', 'post', 'put', 'patch']


# Client specific ViewSet to Add, Update Order for Shopping carts
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        request_body = request.data
        # serializer = self.get_serializer(data=request_body)

        user = User.objects.get(pk=1)
        order = Order.objects.create(user=user,
                                     delivery_date=request_body['delivery_date'],
                                     status=request_body['status'],
                                     total_price=0)
        total_price = 0
        for item in request_body['items']:
            product = Product.objects.get(pk=item['product'])
            quantity = item['quantity']
            order_item = OrderItem.objects.create(product=product, quantity=quantity)
            order.items.add(order_item)
            total_price += product.price * quantity

        order.total_price = total_price
        order.save()

        return Response(f"Order created with #: {order.id}", status=status.HTTP_201_CREATED)
