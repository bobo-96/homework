from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from post.models import Post
from post.serialisers import PostSerializer


class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        Post.objects.create(
            title=request.data.get('title'),
            body=request.data.get('body'),
        )
        return Response('ok')

    def update(self, request, *args, **kwargs):
        instance = Post.objects.get(id=self.kwargs['pk'])
        instance.title = self.request.data.get('title')
        instance.body = self.request.data.get('body')
        instance.save()
        return Response('ok')

    def destroy(self, request, *args, **kwargs):
        instance = Post.objects.get(id=self.kwargs['pk'])
        instance.delete()
        return Response('Deleted')
