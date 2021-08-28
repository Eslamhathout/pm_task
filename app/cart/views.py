from cart import serializers
from cart.models import Cart
from rest_framework import (authentication, generics, mixins, permissions,
                            viewsets)
from rest_framework.authtoken.views import ObtainAuthToken


class CartViewSet(viewsets.ModelViewSet):
    """Manage Carts in the DB"""
    queryset = Cart.objects.all()
    serializer_class = serializers.CartSerializer
    # authentication_classes = (authentication.TokenAuthentication,)
    # permisson_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """Retrieve the carts for auth users"""
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializers):
        """Create a new Cart order """
        serializer.save(user=self.request.user)
