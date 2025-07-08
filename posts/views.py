from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from .serializers import PostSerializer
from rest_framework import generics, permissions


@login_required
def post_message(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "post_message.html", {"form": form})



def view_posts(request):
    if not request.user.is_authenticated:
        return redirect("login")  # Redirect to login page if user is not logged in

    posts = Post.objects.filter(visibility="public") | Post.objects.filter(author=request.user)

    return render(request, "posts/posts.html", {"posts": posts})


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(visibility="public") | Post.objects.filter(author=user)