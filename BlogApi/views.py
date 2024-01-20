from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
@api_view(http_method_names=['GET', 'POST'])
def homepage(request:Request):
    if(request.method=='POST'):
        data=request.data
        response={"message":"Hello World"}
        return Response(data=response, status=status.HTTP_201_CREATED)

    return Response(data={"message":"Welcome"}, status=status.HTTP_200_OK)