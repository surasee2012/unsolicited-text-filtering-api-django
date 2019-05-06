from rest_framework import serializers

class StringListField(serializers.ListField):
    child = serializers.CharField()

class ReqSerializer(serializers.Serializer):
    clfs = StringListField()
    prob = serializers.IntegerField()
    texts = StringListField()
    