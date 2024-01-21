from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from rest_framework import status
from .models import Post
from .Serializers import PostSerializers
from django.shortcuts import get_object_or_404



# Create your views here.
@api_view(http_method_names=['GET', 'POST'])
def homepage(request:Request):
    if(request.method=='POST'):
        data=request.data
        response={"message":"Hello World", "data":data}
        return Response(data=response, status=status.HTTP_201_CREATED)

    return Response(data={"message":"Welcome"}, status=status.HTTP_200_OK)



# Function based views
# @api_view(http_method_names=['GET', 'POST'])
# def list_Posts(request:Request): 
#   posts=Post.objects.all()
#   if request.method=='POST':
#      data=request.data
#      serializer=PostSerializers(data=data)
#      if serializer.is_valid():
#         serializer.save()
#         response={"message":"Posts created", "data":serializer.data}
#         return Response(data=response, status=status.HTTP_201_CREATED)
#      return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#   serializer=PostSerializers(instance=posts, many=True)
#   response={"message":"posts", "data":serializer.data}
#   return  Response(data=response, status=status.HTTP_200_OK)


class PostlistCreateView(APIView):
    """GET AND  CREATE POSTS"""
    serializers_class=PostSerializers
    def get(self, request:Request, *args, **kwargs):
        posts=Post.objects.all()
        serializers=self.serializers_class(instance=posts, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)
    
    def post(self, request:Request, *args, **kwargs):
        data=request.data
        serializers=self.serializers_class(data=data)
        if serializers.is_valid():
            serializers.save()
            response={"message":"Post created successfully", "data":serializers.data}
            return Response(data=response, status=status.HTTP_200_OK)



# @api_view(http_method_names=['GET'])
# def post_detail(request:Request, post_id:int): 
#   post = get_object_or_404(Post, pk=post_id)
#   serializer=PostSerializers(instance=post)
#   response={"message":"post", "data":serializer.data}
#   return  Response(data=response, status=status.HTTP_200_OK)

 
# @api_view(http_method_names=['PUT'])
# def update_post(request:Request, post_id:int):
#     post = get_object_or_404(Post, pk=post_id)
#     data=request.data
#     serializer=PostSerializers(instance=post,data=data)
#     if serializer.is_valid():
#        serializer.save()
#        response={
#        "message":"Post updated successfully",
#        "data":serializer.data}
#        return Response(data=response, status=status.HTTP_200_OK)
#     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(http_method_names=['DELETE'])
# def delete_post(request:Request, post_id:int):
#     post = get_object_or_404(Post, pk=post_id)
#     post.delete()
#     return Response(data={"messaage":"Deleted"}, status=status.HTTP_204_NO_CONTENT)


class PostRetrieveUpdateDeleteView(APIView):
    serializers_class=PostSerializers

    def get(self, request:Request, post_id:int):
        post=get_object_or_404(Post, pk=post_id)
        serializer=self.serializers_class(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
   

    def put(self, request:Request, post_id:int):
        post=get_object_or_404(Post, pk=post_id)
        data=request.data
        serializer=self.serializers_class(instance=post, data=data)
        if serializer.is_valid():
            serializer.save()
            response={
       "message":"Post updated successfully",
       "data":serializer.data}
            return Response(data=response, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

    def delete(self, request:Request, post_id:int):
        post = get_object_or_404(Post, pk=post_id)
        post.delete()
        return Response(data={"messaage":"Deleted"}, status=status.HTTP_204_NO_CONTENT)
  
