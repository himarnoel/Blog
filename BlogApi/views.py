from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status



data_list = [
    {
        'id': 1,
        'title': 'First Entry',
        'contents': 'This is the contents of the first entry.'
    },
    {
        'id': 2,
        'title': 'Second Entry',
        'contents': 'This is the contents of the second entry.'
    },
    {
        'id': 3,
        'title': 'Third Entry',
        'contents': 'This is the contents of the third entry.'
    },
    # Add more entries as needed
]

# Create your views here.
@api_view(http_method_names=['GET', 'POST'])
def homepage(request:Request):
    if(request.method=='POST'):
        data=request.data
        response={"message":"Hello World", "data":data}
        return Response(data=response, status=status.HTTP_201_CREATED)

    return Response(data={"message":"Welcome"}, status=status.HTTP_200_OK)




@api_view(http_method_names=['GET'])
def list_Posts(request:Request): 
  return  Response(data=data_list, status=status.HTTP_200_OK)




@api_view(http_method_names=['GET'])
def post_detail(request:Request, post_index:int): 
  post= data_list[post_index]
  if post:
     return  Response(data=data_list, status=status.HTTP_200_OK)
  
  return  Response(data={"error":"The data not found"}, status=status.HTTP_404_NOT_FOUND)