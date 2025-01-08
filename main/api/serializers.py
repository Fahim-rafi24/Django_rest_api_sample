from rest_framework import serializers
from .models import User, Company, CompanyTargeted, UserUploadPictureInServer


class UserSerializer(serializers.ModelSerializer):   # user
    class Meta:
        model = User
        exclude = ["password"]  # Don't expose the password field


class CompanySerializer(serializers.ModelSerializer):   # company
    class Meta:
        model = Company
        fields = "__all__"


class CompanyTargetedSerializer(serializers.ModelSerializer):   # company all user
    class Meta:
        model = CompanyTargeted
        fields = "__all__"


class UserUploadPictureInServerSerializer(serializers.ModelSerializer):   # user store photo
    class Meta:
        model = UserUploadPictureInServer
        fields = "__all__"