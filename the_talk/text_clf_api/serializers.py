from rest_framework import serializers

class StringListField(serializers.ListField):
    child = serializers.CharField()

class TextSerializer(serializers.Serializer):
    texts= StringListField()