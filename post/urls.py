from django.urls import path
from post.views import PostView

urlpatterns = [
    path('', PostView.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>', PostView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]