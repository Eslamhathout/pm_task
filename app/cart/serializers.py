from rest_framework import serializers
from cart.models import Cart
from catalog.models import Dog

class CartSerializer(serializers.ModelSerializer):
    """Serializer for Cart objects"""

    class Meta:
        model = Cart
        fields = ('id', 'purchase_date', 'delivery_method', 'payment_method', 'dog')
        read_only_fields = ('id',)
