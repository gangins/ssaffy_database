from django.shortcuts import render, get_list_or_404, get_object_or_404
from .serializers import ArticleSerilalizer,CommentSerializer
from .models import Article, Comment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here

#데코레이터 
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == "GET":

        # articles =Article.objects.all 이랑 같음 
        articles = get_list_or_404(Article)
        ArticleSerilalizer(articles, many = True)

        serializer = ArticleSerilalizer(articles, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
    # 반환할때Response class,응답 Status 모듈

        serializer= ArticleSerilalizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors)



@api_view(['GET','DELETE','PUT'])
def article_detail(request, article_pk):
    # article =Article.objects.get(pk=article_pk) #if 를하든 elif 를 하든 같음 
    article= get_object_or_404(Article, pk=article_pk)
    
    
    if request.method=='GET':
    
        serializer = ArticleSerilalizer(instance=article)
        return Response(serializer.data)

    elif request.method =='PUT':
        serializer = ArticleSerilalizer(article, request.data)
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response(serializer.data)


    elif request.method == 'DELETE':
        
        article.delete()
        msg={'delete': f'{article}'}
        return Response(msg,status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def comment_list(request):
    if request.method == "GET":
        comments =get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def comment_detail(request,comment_pk):
    if request.method == "GET":
        comment = Comment.objects.get(pk=comment_pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)


@api_view(['POST'])
def comment_create(request,article_pk):

    article = get_object_or_404(Article, article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data)

    # if request.method == 'GET':
    
   
    #     serializer = ArticleListSerializer(article)
    #     return Response(serializer.data)
    # elif request.method == 'DELETE':
        
    #     article.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)# 다지워서 괄호드가기 어려움
    
    # elif request.method =='PUT':
    #     serializer = ArticleListSerializer(article, data=request.data)
    #     if serializer.is_valid(raise_exception= True):
    #         serializer.save()
    #         return Response(serializer.data)
        