from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

from other_info.models import UserInfo, News, NewData

from other_info.serializers import UserInfoSerializer, NewsSerializer, UserSerializer, NewDataSerializer


class UserInfoViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        info_serializer = UserInfoSerializer(UserInfo.objects.filter(user=request.user.id), many=True)
        user_serializer = UserSerializer(User.objects.filter(id=request.user.id), many=True)
        return Response({'info': info_serializer.data, 'user': user_serializer.data})


class NewsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        info_serializer = NewsSerializer(News.objects.all(), many=True)
        return Response(info_serializer.data)


class NewData(ModelViewSet):
    queryset = NewData.objects.all()
    permission_classes = [AllowAny]
    http_method_names = ['get', 'post', 'put', 'patch']
    serializer_class = NewDataSerializer
