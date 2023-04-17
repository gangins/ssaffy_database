from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Article,Comment
from .serializers import ArticleListSerializer,CommentSerializer


# Create your views here.
@api_view(['GET','POST'])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_201_BAD_REQUEST)

@api_view(['GET','DELETE','PUT'])
def article_detail(request, article_pk):
    article =Article.objects.get(pk=article_pk) #if 를하든 elif 를 하든 같음 
    if request.method == 'GET':
    
   
        serializer = ArticleListSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)# 다지워서 괄호드가기 어려움
    
    elif request.method =='PUT':
        serializer = ArticleListSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response(serializer.data)
        

@api_view(['GET'])
def comment_list(request):
    if request.method == "GET":
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def comment_detail(request,comment_pk):
    if request.method == "GET":
        comment = Comment.objects.get(pk=comment_pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)