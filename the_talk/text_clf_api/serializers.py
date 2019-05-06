from rest_framework import serializers

class StringListField(serializers.ListField):
    child = serializers.CharField()

class TextsSerializer(serializers.Serializer):
    texts = StringListField()
    clfs = StringListField()