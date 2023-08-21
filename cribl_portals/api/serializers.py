from rest_framework import serializers
from elastic.models import ElasticDestination

# class ViewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cluster
#         fields = "__all__"

# class AddSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cluster
#         fields = "title", "description", "username", "password", "url"

class ElasticSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    title = serializers.CharField()
    description = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    url = serializers.CharField()
    message = serializers.CharField()
    status = serializers.IntegerField()

    def create(self, validated_data):
        return ElasticDestination(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.url = validated_data.get('url', instance.url)
        instance.message = validated_data.get('message', instance.message)
        return instance