from django.urls import path
from . import views

urlpatterns = [
    path('', views.booksPage, name='viewBooks'),
    path('details/<int:id>', views.bookDetails, name='bookDetails'),
    path('borrowedBooks', views.borrowedBooksPage, name='view_borrowed_book'),
    
    path('<int:id>', views.borrow, name='borrowBook'),
    path('unBorrow/<int:id>', views.unBorrow, name='unBorrowBook'),

    path('add', views.addBook, name='addBook'),
    path('update/<int:id>', views.update, name='editBook'),
    path('delete/<int:id>', views.delete, name='delBook'),


    path('search/' , views.search_results , name="search")

]