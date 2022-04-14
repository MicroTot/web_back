from django.contrib.auth.models import User
from rest_framework import fields, serializers
from main.models import User_Category, Jobs
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class User_Cat_Serializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = User_Category
        fields = "__all__"


class Jobs_Serializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Jobs
        fields = "__all__"