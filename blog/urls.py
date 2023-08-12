from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import HomePageView,PostDetailPageView,NewPostPageView,EditPostPageView,DeletePostPageView
urlpatterns = [
    path('', HomePageView.as_view() ,name='home'),
    path('post/<int:pk>/',PostDetailPageView.as_view(),name='post_detail'),
    path('post/new',NewPostPageView.as_view(),name='new_post'),
    path('post/<int:pk>/edit',EditPostPageView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete',DeletePostPageView.as_view(),name='post_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)