from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostsViewSet

router = SimpleRouter()
router.register(r'posts', PostsViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'follow', FollowViewSet, basename='follow')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
