from django.shortcuts import render
from django.middleware.csrf import get_token
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Blog
from rest_framework import status
from django.shortcuts import get_object_or_404


#/blogs/index_blogs/
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def index_blogs(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


#/blogs/:blog_id
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_blog(request, blog_id):
     blog = get_object_or_404(Blog, pk = blog_id)
     serializer = BlogSerializer(blog)
     return Response(serializer.data, status=status.HTTP_200_OK)


#/blogs/create/
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_blog(request):
    serializer = UpdateCreateBlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_blog(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    # Check if the user is the owner of the blog
    if blog.author != request.user:
        return Response(
            {'error': 'You are not allowed to update this blog.'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    serializer = UpdateCreateBlogSerializer(blog, data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    # Check if the user is the owner of the blog
    if blog.author != request.user:
        return Response(
            {'error': 'You are not allowed to update this blog.'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    blog.delete()
    return Response(status=status.HTTP_200_OK)

#/blogs/get-csrf-token/
def csrf_token_view(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})

#/blogs/current_user/
@api_view(["GET"])
def current_user(request):
    user = request.user 
    serializer = UserSerializer(user, many = False)
    return Response(serializer.data)
