from django.shortcuts import render, redirect, get_object_or_404

# from webapp.forms import ArticleForm
from webapp.models import Book, StatusChoices


def detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book.html', context={'book': book})
