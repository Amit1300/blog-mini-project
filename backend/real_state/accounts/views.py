from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .models import BlogPost
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serialzer import BlogPostSerializer,Userserializer
from rest_framework.parsers import JSONParser,FormParser,MultiPartParser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.decorators import parser_classes

import json


    
class Blog(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser,FormParser,MultiPartParser]
    def get(self,request):
        blog = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog, many=True)
        return Response(serializer.data)

    def post(self,request):
        user=User.objects.get(username=request.user)
        newdata=request.data
        newdata["user"]=request.user.id
        print(request.user.id)
        serializer = BlogPostSerializer(data=newdata)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

            
                

    def put(self, request, id):
    
        blog =BlogPost.objects.get(id=id)
        if blog.user==request.user:
            serializer =BlogPostSerializer(blog, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"msg":"forbidden"})

    def delete(self,request,id):
        try:
            blog=BlogPost.objects.get(id=id)
            print(blog.user,request.user)
            if blog.user==request.user:
                BlogPost.objects.filter(id=id).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"msg":"not allow"})
                
           
            
        except :
            f={"msg":"no delete"}
            print(type(f))
            return Response(f)
       



        
       
from django.contrib.auth import authenticate, login

@csrf_exempt
@api_view(["POST"])
@permission_classes([AllowAny])
def Signup(request):
    if request.method=="POST":
        users=User.objects.all()
        print(users)
        newuser=Userserializer(data=request.data)
        if newuser.is_valid():
            for user in users:
                print(user.username,user.email,user.password)
                if (((user.email!=request.data["email"]) and (user.password!=request.data["password"] ))and (user.username!=request.data["username"])):
                    newuser.save()
                    return Response(newuser.data)
                else:
                    return Response({"msg":"exits"})

        
    
        
        
                 
        
           
            

   
   
    

        
