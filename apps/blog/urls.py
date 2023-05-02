from django.urls import path
from apps.blog.views import blog,blog_delete,Blog_detail

urlpatterns = [
    path('blog_detail/<int:id>/',Blog_detail.as_view(),name='blog_detail'),
    path('blog/',blog,name='blog'),
    path('blog_delete/',blog_delete,name='blog_delete')
]
