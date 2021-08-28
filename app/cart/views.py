from rest_framework import viewsets, mixins
from cart.models import Cart
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from cart import serializers


class CartViewSet(viewsets.ModelViewSet):
    """Manage Carts in the DB"""
    queryset = Cart.objects.all()
    serializer_class = serializers.CartSerializer
    # authentication_classes = (authentication.TokenAuthentication,)
    # permisson_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """Retrieve the carts for auth users"""
        return self.queryset.filter(user=self.request.user)
