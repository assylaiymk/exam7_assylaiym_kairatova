from django.shortcuts import render, redirect, get_object_or_404
from webapp.forms import BookForm
from webapp.models import Book, StatusChoices


def add_view(request):
    form = BookForm()
    if request.method == 'GET':
        return render(request, 'book_create.html', context={'choices': StatusChoices.choices, 'form': form})
    form = BookForm(request.POST)
    if not form.is_valid():
        print(form.errors)
        return render(request, 'book_create.html', context={'choices': StatusChoices.choices, 'form': form})
    article = Book.objects.create(**form.cleaned_data)
    return redirect('index')


def detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book.html', context={'book': book})


def searchbar_view(request):
    if request.method == 'POST':
        search = request.POST['search']
        books = Book.objects.filter(name__contains=search)
        return render(request, 'searchbar.html', context={'search': search, 'books': books})
    else:
        return render(request, 'searchbar.html', context={})


def update_view(request, pk):
    errors = {}
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        if request.POST.get('name', 'email'):
            errors['name']: "The field is required"
            errors['email']: "The field is required"
        book.name = request.POST.get('name')
        book.email = request.POST.get('email')
        book.author = request.POST.get('author')
        book.text = request.POST.get('text')
        if errors:
            return render(
                request,
                'book_update.html',
                context={
                    'book': book,
                    'choices': StatusChoices.choices,
                    'errors': errors
                })
        book.save()
        return redirect('index')
    return render(
        request,
        'book_update.html',
        context={
            'book': book,
            'choices': StatusChoices.choices,
        })


def delete_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_confirm_delete.html', context={'book': book})


def confirm_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('index')
