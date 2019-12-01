from django.urls import path, include

from .views import NotesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('notes', NotesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]