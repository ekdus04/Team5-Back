from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, post_like_api_view


router = DefaultRouter()
router.register(r'', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('like/<int:post_id>/', post_like_api_view, name='post-like'),
    # path('my/', MyPost.as_view(), name='my-post'),
]