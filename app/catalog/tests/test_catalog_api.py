from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from model_mommy import mommy

from catalog.models import Pet, Dog, Breed
from catalog.serializers import DogSerializer, PetSerializer

PET_URL = reverse('catalog:pet-list')
DOG_URL = reverse('catalog:dog-list')

class PublicDogApiTests(TestCase):
    """Test dog list is avaialable without for any user"""

    def setUp(self):
        self.client = APIClient()
    
    def test_login_not_required_for_dog_listing(self):
        """Test that login is not required for dogs list"""
        res = self.client.get(DOG_URL)
        self.assertNotEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_dogs_list(self):
        """Test retreving dog listing"""
        pet_obj = mommy.make(Pet)
        breed_obj = mommy.make(Breed)
        dog_obj = mommy.make(Dog, breed=breed_obj, pet=pet_obj)

        res = self.client.get(DOG_URL)

        dogs = Dog.objects.all().order_by('id')
        serializer = DogSerializer(dogs, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieve_pets_list(self):
        """Test retreving pet listing"""
        mommy.make(Pet)

        res = self.client.get(PET_URL)

        pets = Pet.objects.all().order_by('id')
        serializer = PetSerializer(pets, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_pet_successfully(self):
        """Test creating a new pet"""
        payload = {'pet_type': 'd', 'pet_feature': 'f'}

        res = self.client.post(PET_URL, payload)

        is_new_pet_exists = Pet.objects.filter(pet_type=payload['pet_type']).exists()
        self.assertTrue(is_new_pet_exists)

    def test_create_pet_invalid(self):
        """Test creating a new pet with invald data. """
        payload = {}

        res = self.client.post(PET_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
