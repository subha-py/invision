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
                #todo: fill me up
            }
        )

class GameCategoryList(ListCreateAPIView):
    pass