from django.shortcuts import render

from webapp.models import Book, StatusChoices


def index_view(request):
    books = Book.objects.exclude(is_deleted=True).order_by('-created_at').filter(status='ACTIVE')
    context = {
        'books': books
    }
    return render(request, 'index.html', context)
