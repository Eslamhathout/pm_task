from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from cart.models import Cart

from cart.serializers import CartSerializer


CART_URL = reverse('cart:cart-list')


def sample_cart(user, **params):
    """Create and return a sample cart"""
    defaults = {
        'delivery_method': 'Nearest Pickup',
        'payment_method': 'CoD'
    }
    #For updating defaults dict
    defaults.update(params)

    return Cart.objects.create(user=user, **defaults)


class PrivateCartAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'pmpm@gmail.com',
            'testpassword'
        )

        self.client.force_authenticate(self.user)


    def test_retrieve_orders(self):
        """Test retrieving a list of orders"""
        sample_cart(user=self.user)
        sample_cart(user=self.user)

        res = self.client.get(CART_URL)

        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_carts_limited_to_user(self):
        """Test retriving carts for user"""
        user2 = get_user_model().objects.create_user(
            'other@paymob.com',
            'passw1234'
        )

        sample_cart(user=user2)
        sample_cart(user=self.user)

        res = self.client.get(CART_URL)

        carts = Cart.objects.all().filter(user=self.user)
        serializer = CartSerializer(carts, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
        self.assertEqual(len(res.data), 1)

















