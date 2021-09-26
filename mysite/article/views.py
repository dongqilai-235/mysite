from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Article


# def article_detail(request, article_id):
#     article = Article.objects.get(id=article_id)
#     return render(request, "article_detail.html", {"articleobj": article})
def article_list(request):
    articles = get_list_or_404(Article)
    return render(request, "article_list.html", {"article_list": articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, "article_detail.html", {"article_obj": article})


