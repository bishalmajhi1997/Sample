from rest_framework import serializers
from authentication.models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils .encoding import smart_str,force_str,smart_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68,min_length=10,write_only=True)
    class Meta:
        model=User
        fields=('email','username','password')
    def validate(self,attrs):
        email=attrs.get('email','')
        username=attrs.get('username','')
        if not username.isalnum():
            raise serializers.ValidationError("the username should contain alphanumeric charecters.")
        return attrs
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']
class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255,min_length=3)
    password=serializers.CharField(max_length=68,min_length=8,write_only=True)
    username=serializers.CharField(max_length=68,min_length=8,read_only=True)
    tokens=serializers.CharField(max_length=68,min_length=8,read_only=True)

    class Meta:
        model=User
        fields=["email","password","username","tokens"]
    def validate(self,attrs):
        email=attrs.get("email","")
        password=attrs.get("password","")
        user=auth.authenticate(email=email,password=password)
        if not user:
            raise AuthenticatiinFailed("Invalid credentials,try again")
        if not user.is_active:
            raise AuthenticatiinFailed("Account disabled,contract admin")
        if not user.is_verified:
            raise AuthenticatiinFailed("Email is not verified.")
        return {
           'email':user.email,
           'username':user.username,
           'tokens':user.tokens
        }
        return super().validate(attrs)
class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email=serializers.EmailField(min_length=2)
    class Meta:
        fields=["email"]
class SetNewPasswordSerializer(serializers.Serializer):
    password=serializers.CharField(min_length=1,max_length=68,write_only=True)
    token=serializers.CharField(min_length=1,write_only=True)
    uid64=serializers.CharField(min_length=1,write_only=True)
    class Meta:
        fields=["password","token","uid64"]
        def validate(self,attrs):
            try:
                password=attrs.get('password')
                token=token.get('token')
                uid64=attrs.get('uid64')
                id=force_str(urlsafe_base64_decode(uid64))
                user=User.objects.get(id=id)
                if not PasswordResetTokenGenerator().check_token(user,token):
                    raise AuthenticationFailed('The reset link is invalid.',401)
                user.set_password(password)
                user.save()
                return user
            except  Exception as e:
                raise AutAuthenticationFailed("The reset link is invalid.",401)

            return super().validate(attrs)
