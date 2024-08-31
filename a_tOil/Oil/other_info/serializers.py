from rest_framework import serializers
from django.contrib.auth.models import User

from other_info.models import UserInfo, News


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['user', 'table_access', 'user_photo', 'some_info']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['news_header', 'news_body','news_image']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
