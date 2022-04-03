from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, PublisherViewSet

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('publishers', PublisherViewSet)

urlpatterns = router.urls