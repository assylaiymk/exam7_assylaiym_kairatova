from django.contrib import admin
from webapp.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'author', 'created_at')
    list_filter = ('id', 'name', 'email', 'author', 'created_at')
    search_fields = ('name', 'author')
    fields = ('name', 'author', 'text', 'created_at', 'changed_at')
    readonly_fields = ('id', 'created_at', 'changed_at')


admin.site.register(Book, BookAdmin)
