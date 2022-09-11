from rest_framework import serializers

from plans.models import Plan


class PlanSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = Plan
        fields = ['user', 'items']

    @staticmethod
    def get_items(obj):
        return PlanItemSerializer(obj.items.all(), many=True).data


class PlanItemSerializer(serializers.Serializer):
    title = serializers.CharField(source='content_object.title')
    description = serializers.CharField(source='content_object.description')
