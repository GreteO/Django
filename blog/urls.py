from . import views
from django.urls import path
from blog.views import CreatePostView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('blog/templates/', CreatePostView.as_view(), name='newpost')
]