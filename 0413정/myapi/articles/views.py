from django.shortcuts import render, get_object_or_404,get_list_or_404
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

#api 처리는 무조건 데코
@api_view(['GET',])
def article_list(request):
    articles = Article.objects.all()
    # articles = get_list_or_404(Article)
    serializer=ArticleSerializer(articles, many=True)

    return Response(serializer.data)

@api_view(['GET','PUT','DELETE',])
def article_detail(request, article_pk):
    if request.method =='GET':
        article = get_object_or_404(Article, pk=article_pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method =='PUT':
        pass
    elif request.method =='DELETE':
        article.delete()
        msg={'delete':f'{article_pk}번 게시글 삭제'}
        return Response(msg)
    
