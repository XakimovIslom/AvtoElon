from rest_framework import serializers
from option.models import (
    Option,
    PostOption,
    OptionValue,
    OptionValueExtended,
    PostOptionValue,
)


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = "__all__"


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionValue
        fields = "__all__"


class PostOptionValueSerializer(serializers.ModelSerializer):
    option_value = ValueSerializer()

    class Meta:
        model = PostOptionValue
        fields = "__all__"


class PostOptionSerializer(serializers.ModelSerializer):
    option = OptionSerializer()
    values = PostOptionValueSerializer(many=True)

    class Meta:
        model = PostOption
        fields = ("option", 'value', "values")
