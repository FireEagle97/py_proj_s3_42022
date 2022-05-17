from rest_framework.serializers import ModelSerializer
from .models import Item, Review
from django.contrib.auth.models import User, Group

class ItemClassSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

class ReviewClassSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"