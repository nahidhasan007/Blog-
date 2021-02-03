from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, CommentView

urlpatterns = [
#  path('',views.home, name="home"),
  path('',HomeView.as_view(), name="home"),
  path('article/<int:pk>/', ArticleDetailView.as_view(),name='article_details'),
  path('addpost/',AddPostView.as_view(),name="addpost"),
  path('article/update/<int:pk>/',UpdatePostView.as_view(),name="updatepost"),
  path('article/<int:pk>/delete/',DeletePostView.as_view(),name="deletepost"),
  #path('article/<int:pk>/comment/',CommentPostView.as_view(),name='commentpost'),
  path('article/<int:pk>/comment/',CommentView.as_view(),name='commentpost')
]