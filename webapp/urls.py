from django.urls import path
from webapp.views.books import add_view, detail_view, update_view, delete_view, confirm_delete
from webapp.views.base import index_view

urlpatterns = [
    path('', index_view, name='index'),
    path('books/add/', add_view, name='book_add'),
    path('books/<int:pk>/update/', update_view, name='book_update'),
    path('books/<int:pk>/delete/', delete_view, name='book_delete'),
    path('books/<int:pk>/confirm-delete/', confirm_delete, name='confirm_delete'),
    path('books/', index_view),
    path('books/<int:pk>', detail_view, name='book_detail')
]