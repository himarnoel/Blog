from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Post (models.Model):
    title=models.CharField(max_length=50)
    content= models.TextField()
    created =models.DateTimeField(auto_now_add=True)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")

    def __str__(self) -> str:
        return self.title

    # class Meta:
    #     ordering = ["-created"]