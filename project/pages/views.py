from django.shortcuts import render
from books.models import Book, Category
# Create your views here.
def homePage(request):
    current_user = request.user
    isAdmin = current_user.is_staff if current_user.is_authenticated else False
    isNotSignedIn = not current_user.is_authenticated
    return render(request, 'pages/Home.html', {'books':Book.objects.all().order_by('name'), 'cat': Category.objects.all(), 'isAdmin': isAdmin, 'isNotSignedIn': isNotSignedIn})