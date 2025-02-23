# from rest_framework import serializers
# from rest_framework import serializers
# from django.contrib.auth.models import User
# from rest_framework_simplejwt.tokens import RefreshToken

# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, min_length=8)

#     class Meta:
#         model = User
#         fields = ['username','first_name','last_name', 'email', 'password']

#     def create(self, validated_data):
#         # Create user instance
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last'],
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#         return user

    

#     # serializers.py
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         #token['id'] = user.id
#         #token['email'] = user.email

#         return token



from rest_framework import serializers
from .models import Customer
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'password', 'dob', 'mobile', 'gender', 'type']

    def create(self, validated_data):
        user = Customer.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            dob=validated_data["dob"],
            mobile=validated_data["mobile"],
            gender=validated_data["gender"],
            type=validated_data["type"],
        )
        return user


from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Customer

class CustomerLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if not email or not password:
            raise AuthenticationFailed("Email and password are required.")

        user = authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed("Invalid credentials.")

        if not user.is_active:
            raise AuthenticationFailed("User account is not active.")

        return {"user": user}



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "email"  # 🔹 Ensure authentication uses email

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if not email or not password:
            raise AuthenticationFailed("Email and password are required.")

        try:
            user = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            raise AuthenticationFailed("Invalid credentials.")

        if not user.check_password(password):
            raise AuthenticationFailed("Invalid credentials.")

        if not user.is_active:
            raise AuthenticationFailed("User account is not active.")

        # Generate JWT tokens manually
        # refresh = RefreshToken.for_user(user)
        # access_token = str(refresh.access_token)
        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token 

        refresh["user_id"] = user.id
        access_token["user_id"] = user.id

        return {
            "access": str(access_token),
            "refresh": str(refresh),
            "user": {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
            }
        }
