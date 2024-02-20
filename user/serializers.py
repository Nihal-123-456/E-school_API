from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfoModel
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','password']

class RegistrationSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=ROLE, required=True)
    image = serializers.ImageField(required=True)
    confirm_password = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['role','username','first_name','last_name','email','image','password','confirm_password']
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        role = self.validated_data['role']
        image = self.validated_data['image']

        if password != confirm_password:
            raise serializers.ValidationError({"error":"Password does not match"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error":"Email already exists"})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"error":"Username already exists"})
        
        account = User(username=username, email=email, first_name=first_name, last_name=last_name)
        account.set_password(password)
        account.is_active = False
        account.save()
        userinfo = UserInfoModel(user=account, role=role, image=image)
        userinfo.save()
        return account

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

        

        