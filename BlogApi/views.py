from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
@api_view(http_method_names=['GET', 'POST'])
def homepage(request:Request):
    if(request.method=='GET'):


    return Response(data={"message":"Welcome"})