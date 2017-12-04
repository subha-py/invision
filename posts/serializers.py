from rest_framework import serializers
from posts.models import (
    Post,
    Photo
)

class PostSerialzer(serializers.HyperlinkedModelSerializer):
    photos = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='photo-detail'
    )

    class Meta:
        model = Post
        fields = (
            'url',
            'pk',
            'title',
            'description',
            'price',
            'latitude',
            'longitude',
            'make_offer',
            'photos'
        )

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.SlugRelatedField(
        queryset=Post.objects.all(),
        slug_field='title',
    )

    class Meta:
        model = Photo
        fields = (
            'url',
            'post',
            'name',
            'size',
            'image',
        )
