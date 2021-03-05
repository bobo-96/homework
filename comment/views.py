from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from comment.models import Comment
from comment.serialisers import CommentSerializer


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        Comment.objects.create(
            content=request.data.get('content'),
        )
        return Response('ok')

    def update(self, request, *args, **kwargs):
        instance = Comment.objects.get(id=self.kwargs['pk'])
        instance.content = self.request.data.get('content')
        instance.save()
        return Response('ok')

    def destroy(self, request, *args, **kwargs):
        instance = Comment.objects.get(id=self.kwargs['pk'])
        instance.delete()
        return Response('Deleted')
