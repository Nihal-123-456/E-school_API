from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('ownedcourses',OwnedCoursesView)
router.register('wishlist', WishlistView)
router.register('cart', CartView)
router.register('review', ReviewView)

urlpatterns = [
    path('',include(router.urls))
]
