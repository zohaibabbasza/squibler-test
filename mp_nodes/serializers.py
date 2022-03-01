from django.contrib.auth.models import User
from rest_framework import serializers
from mp_nodes import models
from sections.serializers import UserSerializer


class TreeSectionChildSerializer(serializers.ModelSerializer):
    sub_section = serializers.SerializerMethodField()

    def get_sub_section(self,obj):
        return TreeSectionChildSerializer(models.TreeSection.objects.filter(path__startswith=obj.path,
                                       depth=obj.depth+1),many=True).data
    class Meta:
        model = models.TreeSection
        fields = ('id','path','depth','numchild','title','body','sub_section')

class TreeSectionSerializer(serializers.ModelSerializer):
    sub_section = serializers.SerializerMethodField()
    collaboration = UserSerializer(many=True, required=False)
    owner = UserSerializer(required=False)
    parent_id = serializers.CharField(required=False)
    path = serializers.CharField(required=False)
    depth = serializers.CharField(required=False)

    def get_sub_section(self,obj):
        return TreeSectionChildSerializer(models.TreeSection.objects.filter(path__startswith=obj.path,
                                       depth=obj.depth+1),many=True).data
    class Meta:
        model = models.TreeSection
        exclude = ('created_date',)

    def create(self, validated_data):
        user = self.context["request"].user
        if 'parent_id' not in validated_data:
            data = models.TreeSection.add_root(**validated_data)
        else:
            data = models.TreeSection.objects.get(id=validated_data.pop('parent_id'))
            data.add_child(**validated_data)
        return data
    