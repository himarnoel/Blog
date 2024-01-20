from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Post
from .Serializers import PostSerializers



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
  posts=Post.objects.all()
  serializer=PostSerializers(instance=posts, many=True)
  return  Response(data=serializer.data, status=status.HTTP_200_OK)




@api_view(http_method_names=['GET'])
def post_detail(request:Request, post_index:int): 

  post = data_list[post_index-1]
  if post:
     return  Response(data=post, status=status.HTTP_200_OK)
  
  return  Response(data={"error":"The data not found"}, status=status.HTTP_404_NOT_FOUND)