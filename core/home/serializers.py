from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username','password']

        def create(self , validated_data):
            user = User.objects.create(username = validated_data['username'])
            user.set_password(validated_data['password'])
            print(user)
            user.save()
            return user
            

class StudenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
