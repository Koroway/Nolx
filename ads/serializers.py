from rest_framework import serializers

from ads.models import Ad, Selection, Category
from users.models import User


class NotTrueValidator:
    def __call__(self, value):
        if value:
            raise serializers.ValidationError("New ad can not be published")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='first_name',
        read_only=True,
    )

    class Meta:
        model = Ad
        fields = ["id", "name", "author_id", "author", "price", "description", "is_published", "category_id", "image"]


class AdCreateSerializer(serializers.ModelSerializer):
    is_published = serializers.BooleanField(validators=[NotTrueValidator()])

    class Meta:
        model = Ad
        fields = '__all__'


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ["id", "name"]


class SelectionDetailSerializer(serializers.ModelSerializer):
    items = AdSerializer(many=True)

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = '__all__'