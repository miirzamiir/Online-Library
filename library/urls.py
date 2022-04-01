from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet

router = DefaultRouter()
router.register('authors', AuthorViewSet)

urlpatterns = router.urls