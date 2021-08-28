from django.db import models
from django.urls import reverse


class Pet(models.Model):
    """Model representing the main Pet Charachtaristics"""
    PET_TYPE = (
        ('d', 'Dogs'),
        ('c', 'Cats'),
        ('b', 'Birds'),
    )

    PET_FEATURE = (
        ('f', 'Fly'),
        ('s', 'Swim'),
        ('r', 'Run'),
    )

    pet_type = models.CharField(
        max_length=1,
        choices=PET_TYPE,
        blank=False,
        help_text='type of the pet',
        default='d',
    )
    pet_feature = models.CharField(
        max_length=1,
        choices=PET_FEATURE,
        blank=False,
        help_text='What pet can do.',
    )

    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'


    def __str__(self):                          
        return f'{self.id}: {self.pet_type} can {self.pet_feature}'


class Breed(models.Model):
    """Model representing supplier of the animal"""
    name = models.CharField(max_length=100)
    country = models.TextField(max_length=1000)

    def get_absolute_url(self):
        """Returns the url to access a particular breed instance."""
        return reverse('breed-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.id}, {self.name}'


class Dog(models.Model):
    """Model representing a specific Pet type > dog"""
    SALE_STATUS = (
        ('a', 'Available'),
        ('u', 'Unavailable'),
        ('r', 'Reserved'),
        ('s', 'Sold'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80, null=False)
    color = models.CharField(max_length=80, null=True)
    age = models.IntegerField(null=True, default=0)
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE, null=True)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=True)
    likes = models.TextField(max_length=1000 ,default="", help_text="A few things the dog likes")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(
        max_length=1,
        choices=SALE_STATUS,
        blank=True,
        default='a',
        help_text='status of the dog',
    )
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this dog."""
        return reverse('dog-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.id}, {self.name}'

