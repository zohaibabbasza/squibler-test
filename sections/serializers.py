from django.contrib.auth.models import User
from rest_framework import serializers
from sections import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
        ]


class SectionSerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()
    collaboration = UserSerializer(many=True, required=False)
    owner = UserSerializer(required=False)
    parent_id = serializers.CharField(required=False)

    def get_parent(self, obj):
        if obj.parent:
            return SectionSerializer(obj.parent).data
        return None

    class Meta:
        model = models.Section
        exclude = ('created_date',)

    def create(self, validated_data):
        user = self.context["request"].user
        if "parent_id" in validated_data:
            parent = models.Section.objects.filter(id=validated_data.pop("parent_id"))
            if parent.exists():
                parent = parent.first()
            else:
                parent = None
            if user == parent.owner or user in parent.collaboration.all():
                validated_data["parent"] = parent
        section = models.Section.objects.create(**validated_data)
        return section
