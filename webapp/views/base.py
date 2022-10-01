from django.shortcuts import render

from webapp.models import Book


def index_view(request):
    books = Book.objects.exclude(is_deleted=True)
    context = {
        'books': books
    }
    return render(request, 'index.html', context)
