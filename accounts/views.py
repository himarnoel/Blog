from django.shortcuts import render
from .serializers import SignupSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request

# Create your views here.
class SignupView(generics.GenericAPIView):
    serializer_class=SignupSerializer

    def post(self, request:Request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response={
                "message":"User created successfully"
            }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)