from rest_framework import serializers

from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    creation_date = serializers.DateTimeField(format='%d-%m-%y %H-%M-%S')

    class Meta:
        model = Post
        fields = ('title', 'body', 'creation_date', 'author')
