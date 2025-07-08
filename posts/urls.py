from django.urls import path
from .views import post_message, view_posts,PostCreateView, PostListView

urlpatterns = [
    path("", view_posts, name="view_posts"),  # /posts/ will now show posts
    path("post/", post_message, name="post_message"),
     path('create/', PostCreateView.as_view(), name='post-create'),
    path('list/', PostListView.as_view(), name='post-list'),
]

