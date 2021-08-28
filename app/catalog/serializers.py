from rest_framework import serializers
from catalog.models import Pet, Dog, Breed

class PetSerializer(serializers.ModelSerializer):
    """Serializer for Pet objects"""
    class Meta:
        model = Pet
        fields = ('id', 'pet_type', 'pet_feature')
        read_only_field = ('id',)


class BreedSerializer(serializers.ModelSerializer):
    """Serializer for Breed objects"""
    class Meta:
        model = Breed
        fields = ('id', 'name', 'country')
        read_only_field = ('id',)


class DogSerializer(serializers.ModelSerializer):
    """Serializer for dog objects"""
    class Meta:
        model = Dog
        fields = ('id', 'name', 'price', 'age','breed', 'status', 'likes', 'pet')
        read_only_field = ('id',)
