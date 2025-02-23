from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.models import Customer  # Import your Customer model
from .serializers import RegisterSerializer, CustomerLoginSerializer, CustomTokenObtainPairSerializer

from datetime import datetime,timezone
from django.utils.timezone import make_aware


class RegisterUserAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "message": "User registered successfully",
            "user": {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "dob": user.dob,
                "mobile": user.mobile,
                "gender": user.gender,
                "type": user.type,
                "is_active": user.is_active,
                "is_staff": user.is_staff,
                "created_at": user.created_at,
                "updated_at": user.updated_at
            }
        }, status=status.HTTP_201_CREATED)




def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class LoginAPIView(generics.GenericAPIView):
    serializer_class = CustomerLoginSerializer
    permission_classes = [permissions.AllowAny]  # No authentication required for this view
    authentication_classes = []  # Disables JWT authentication for this view

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.validated_data['user']
        token = get_tokens_for_user(user)

        user_data = {
            'id': user.id,
            'firstName': user.first_name,
            'lastName': user.last_name,
            'emailId': user.email,
            'mobileNumber': user.mobile,
            'dob': user.dob,
            'gender': user.gender,
            'type': user.type
        }

        return Response({"token": token, "message": "Login Successful"}, status=status.HTTP_200_OK)




# class ValidateTokenAPIView(APIView):
#     permission_classes = [IsAuthenticated] 
#     def get(self, request):

#         user = request.user  

#         try:
#             customer = Customer.objects.get(id=user.id)
#         except Customer.DoesNotExist:
#             return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

#         return Response({
#             "message": "Token is valid",
#             "user": {
#                 "id": customer.id,
#                 "first_name": customer.first_name,
#                 "last_name": customer.last_name,
#                 "email": customer.email,
#             }
#         }, status=status.HTTP_200_OK)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class ValidateTokenAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user  # Get authenticated user
        return Response({
            "user": {
                "id": user.id,
                "firstName": user.first_name,
                "emailId": user.email,
            }
        }, status=status.HTTP_200_OK)
