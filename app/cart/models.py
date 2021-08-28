from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from catalog.models import Dog, Pet, Breed

class Cart(models.Model):
    """Cart model"""

    DELIVERY_METHOD = (
        ('home', 'Home'),
        ('office', 'Office'),
        ('pick-up-station', 'Pick-up-station'),
    )
    PAYMENT_METHOD = (
        ('cod', 'Cash on delivery'),
        ('credit-card', 'Credit-Card'),
        ('wallet', 'Wallet'),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    purchase_date = models.DateTimeField(auto_now_add=True)
    dog = models.OneToOneField(Dog, on_delete=models.CASCADE)
    delivery_method = models.CharField(
        max_length=30,
        choices=DELIVERY_METHOD,
        blank=True,
        default='home',
        help_text='How order should be delivered!',
    )
    payment_method = models.CharField(
        max_length=3,
        choices=PAYMENT_METHOD,
        blank=True,
        default='cod',
        help_text='How order should be paid!',
    )

    def __str__(self):
        return f'{self.id}: {self.purchase_date}'
