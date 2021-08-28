from django.urls import path, include
from rest_framework.routers import DefaultRouter

from catalog import views

router = DefaultRouter()
router.register('dogs', views.DogViewSet)
router.register('pets', views.PetViewSet)
router.register('breeds', views.BreedViewSet)

app_name = 'catalog'

urlpatterns = [
    path('', include(router.urls)),
]