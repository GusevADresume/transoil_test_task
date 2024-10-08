from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from i_table.models import infotable
from i_table.serializers import InfoTableSerializer
from i_table.permissions import IsInTableGroup


class ITableViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsInTableGroup]
    queryset = infotable.objects.all()
    serializer_class = InfoTableSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = '__all__'
    filterset_fields = '__all__'
    search_fields = ['maker', 'model']
    http_method_names = ['get', 'post', 'patch', 'delete', 'put']
    pagination_class = LimitOffsetPagination