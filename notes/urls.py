from django.urls import path, include

from .views import NotesViewSet, notes_user
from rest_framework import routers

router = routers.DefaultRouter()
router.register('notes', NotesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('notes/user/<int:id>', notes_user, name="notes_user"),
]