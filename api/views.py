from django.shortcuts import render
from django.http import HttpResponse
from ebooks_app.models import Book
import json
from .serializers import BookSerializer
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def manual_index(request):
    books = Book.objects.all()
    items = []
    for i in books:
        dic = dict(id=i.pk, name=i.name, isbn=i.isbn)
        items.append(dic)

    books_string = json.dumps(items);    
    return HttpResponse(books_string, content_type='application/json')
