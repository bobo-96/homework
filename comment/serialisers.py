from rest_framework import serializers

from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    creation_date = serializers.DateTimeField(format='%d-%m-%y %H-%M-%S')

    class Meta:
        model = Comment
        fields = ('content', 'creation_date', 'author', 'post')
