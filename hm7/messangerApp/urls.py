from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet, CommentViewSet, MarkCommentViewSet, MarkPostViewSet, \
    SummaryMarkOnPostAPIView, SummaryMarkOnCommentAPIView, CommentsOnPostAPIView, PostsOnUserAPIView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('comments', CommentViewSet)
router.register('posts', PostViewSet)
router.register('mark_posts', MarkPostViewSet)
router.register('mark_comments', MarkCommentViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('summary_mark_post/<int:pk>/', SummaryMarkOnPostAPIView.as_view()),
    path('summary_mark_comment/<int:pk>/', SummaryMarkOnCommentAPIView.as_view()),
    path('comments_on_post/<int:pk>/', CommentsOnPostAPIView.as_view()),
    path('posts_on_user/<int:pk>/', PostsOnUserAPIView.as_view()),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
