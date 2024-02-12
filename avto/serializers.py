from rest_framework import serializers
import json

from avto.models import Post, District
from option.serializers import PostOptionSerializer


class PostSerializer(serializers.ModelSerializer):
    district = serializers.StringRelatedField(source="json.district")
    title = serializers.StringRelatedField(source="json.title", read_only=True)
    extended_title = serializers.StringRelatedField(
        source="json.extended_title", read_only=True
    )
    photo_count = serializers.IntegerField(source="json.photos_count", read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "extended_title",
            "photo_count",
            "main_photo",
            "district",
        )


class PostRetrieveSerializer(serializers.ModelSerializer):
    district = serializers.StringRelatedField(source="district.title")
    title = serializers.StringRelatedField(source="json.title", read_only=True)
    options = serializers.StringRelatedField(source="json.options", read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'price',
                  'district', 'options', 'main_photo', 'info', 'status', 'is_active',
                  )


class PostSimilarSerializer(serializers.ModelSerializer):
    title = serializers.StringRelatedField(source="json.title", read_only=True)
    district = serializers.StringRelatedField(source="district.title")

    class Meta:
        model = Post
        fields = ('title', 'price', 'district')


class PostSubSerializer(serializers.ModelSerializer):
    title = serializers.StringRelatedField(source="json.title", read_only=True)
    district = serializers.StringRelatedField(source="district.title")
    options = serializers.StringRelatedField(source="json.options", read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'options', 'district', 'published_at', 'views', 'price')


class DistrictSerializer(serializers.ModelSerializer):
    posts_count = serializers.SerializerMethodField()

    class Meta:
        model = District
        fields = ('title', 'posts_count')

    def get_posts_count(self, obj):
        return obj.posts.count()


class PostFilterSerializer(serializers.ModelSerializer):
    district = serializers.StringRelatedField(source="district.title")
    marka = serializers.StringRelatedField(source="json.model", read_only=True)
    model_values = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('district', 'marka', 'model_values')

    def get_model_values(self, obj):
        options_str = "Chevrolet Gentra, 3 position"

        # Split the options string by comma
        options_list = options_str.split(',')

        # Iterate over the elements in the options list
        for option in options_list:
            # Trim whitespace from the elements
            option = option.strip()
        return option
