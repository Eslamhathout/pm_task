from rest_framework import viewsets, mixins
from catalog.models import Dog, Pet, Breed

from catalog import serializers


class PetViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Manage Pets in the DB"""
    queryset = Pet.objects.all()
    serializer_class = serializers.PetSerializer


class DogViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Manage dogs in the DB"""
    queryset = Dog.objects.all()
    serializer_class = serializers.DogSerializer


class BreedViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Manage Breeds in the DB"""
    queryset = Breed.objects.all()
    serializer_class = serializers.BreedSerializer