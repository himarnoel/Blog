from . import views

from django.urls import path

urlpatterns = [
    path("homepage/", views.homepage, name="posts_home"),
    path("", views.PostlistCreateView.as_view(), name="list_Post"),
    path("<int:post_id>/", views.PostRetrieveUpdateDeleteView.as_view(), name="post_retreiveupdatedelete"),
  
]


