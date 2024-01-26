from django.shortcuts import render
from .serializers import SignupSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from  rest_framework.views import APIView
from django.contrib.auth import authenticate
# Create your views here.
class SignupView(generics.GenericAPIView):
    serializer_class=SignupSerializer

    def post(self, request:Request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response={
                "message":"User created successfully",
          "data": serializer.data}
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    permission_classes = []

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)

        if user is not None:
            response = {"message": "Login Successfull", "token":""}
            return Response(data=response, status=status.HTTP_200_OK)
        
        else:
            return Response(data={"message": "Invalid email or password"})
    

    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)