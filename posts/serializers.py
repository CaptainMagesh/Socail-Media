from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  # Prevent modification

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'visibility', 'created_at']
