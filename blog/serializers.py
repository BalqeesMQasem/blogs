from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog

# Add user serialzer to show current user.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}    


# Add blog serializer 
# I have 2 different serializers to show blogs with auther data at index and show endpoints.
class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Blog
        fields = '__all__'        
    
class UpdateCreateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'    