from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from other_info.models import UserInfo, News

from other_info.serializers import UserInfoSerializer, NewsSerializer


class UserInfoViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    http_method_names = ['get']


class NewsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    http_method_names = ['get']