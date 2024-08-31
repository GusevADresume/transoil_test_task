from rest_framework import serializers

from i_table.models import infotable


class InfoTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = infotable
        fields = '__all__'