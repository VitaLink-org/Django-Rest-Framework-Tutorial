from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    BookListCreateAPIView,
    BookListCreateGenericAPIView,
    BookRetrieveUpdateDestroyAPIView,
    BookRetrieveUpdateDestroyGenericAPIView,
    BookViewSet,
)

router = DefaultRouter()
router.register("", BookViewSet)

urlpatterns = [
    path("/", BookListCreateAPIView.as_view()),
    path("<int:pk>/", BookRetrieveUpdateDestroyAPIView.as_view()),
    path("generic/", BookListCreateGenericAPIView.as_view()),
    path("generic/<int:pk>/", BookRetrieveUpdateDestroyGenericAPIView.as_view()),
    path("viewsets/", include(router.urls)),
]
