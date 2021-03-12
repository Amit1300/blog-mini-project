from rest_framework import serializers
from .models import BlogPost
from django.contrib.auth.models import User





class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields ="__all__"





class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']



    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
