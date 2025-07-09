from rest_framework import serializers
from .models import Tasks
from django.contrib.auth.models import User



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'  
        read_only_fields = ['owner', 'created_at']

class UserCreating(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  
        }

    def validate_email(self, value):
        # validate of email is unice
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def create(self, validated_data):
        # This fun to cretae the user safly and save password not like string
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])  # 🔐
        user.save()
        return user
