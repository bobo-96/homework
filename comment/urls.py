from django.urls import path
from comment.views import CommentView

urlpatterns = [
    path('', CommentView.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>', CommentView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]