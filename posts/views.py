from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
    ListAPIView,
    RetrieveAPIView
)

from posts.models import Post,Photo
from posts.serializers import PostSerialzer,PhotoSerializer


class ApiRoot(GenericAPIView):
    name = 'api-root'

    def get(self,request, *args, **kwargs):
        return Response(
            {
                'photo': reverse(PhotoList.name,request=request),
                'post': reverse(PostList.name,request=request)
            }
        )

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialzer
    name = 'post-list'

class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialzer
    name = 'post-detail'

class PhotoList(ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    name = 'photo-list'

class PhotoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    name = 'photo-detail'