from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.Serializer):
    class Meta:
        model=Post
        field="__all__"