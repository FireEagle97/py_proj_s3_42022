from rest_framework.serializers import ModelSerializer
from .models import Member
from django.contrib.auth.models import User, Group

class MemberClassSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"

class UserClassSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']