from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('topic', TopicView)
router.register('course', CourseView)

urlpatterns = [
    path('',include(router.urls))
]
