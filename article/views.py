from django.shortcuts import render
from django.http.response import HttpResponse
from models import Article
from django.template import Context, loader
from django.core import serializers

def homepage(request):
    article_list = Article.objects.all()
    json_data = serializers.serialize("json", article_list)
    template = loader.get_template('index.html')
    context = Context({"json": json_data})
    output = template.render(context)
    return HttpResponse(output)
