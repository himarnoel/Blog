from . import views

from django.urls import path

urlpatterns = [
    path("homepage/", views.homepage, name="posts_home"),
    path("", views.list_Posts, name="list_Post"),
    path("<int:post_index>", views.post_detail, name="post_detail")
]


