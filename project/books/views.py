from django.shortcuts import render, redirect
from .models import Book, Category
from .forms import BookForm
from django.contrib.auth.models import User
from django.db.models import Q

from django.http import JsonResponse

# Create your views here.
def booksPage(request):
    title = None
    search = Book.objects.all()
    if 'search' in request.GET:
        title = request.GET.get('search')
        if title:
            search = search.filter(Q(name__icontains = title) | Q(author__icontains = title) | Q(category__name__icontains = title))

    current_user = request.user
    isAdmin = current_user.is_staff if current_user.is_authenticated else False
    isNotSignedIn = not current_user.is_authenticated

    return render(request, 'pages/viewBooks.html', {'books': search, 'cat' : Category.objects.all(), 'isAdmin': isAdmin, 'isNotSignedIn': isNotSignedIn})




def addBook(request):
    if request.method == 'POST':
        data = BookForm(request.POST, request.FILES).save()

    current_user = request.user
    isAdmin = current_user.is_staff if current_user.is_authenticated else False
    isNotSignedIn = not current_user.is_authenticated

    
    return render(request, 'pages/addBook.html', {'BF':BookForm, 'isAdmin': isAdmin, 'isNotSignedIn': isNotSignedIn})




def update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == "POST":
        updated = BookForm(request.POST, request.FILES, instance=book_id)
        if updated.is_valid():
            updated.save()
            return redirect("../../")
    else:
        updated = BookForm(instance=book_id)

    current_user = request.user
    isAdmin = current_user.is_staff if current_user.is_authenticated else False
    isNotSignedIn = not current_user.is_authenticated

    return render(request, 'pages/editBook.html', {'BF':updated, 'isAdmin': isAdmin, 'isNotSignedIn': isNotSignedIn})




def delete(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == "POST":
        book_id.delete()
        return redirect("/books")
    
    current_user = request.user
    isAdmin = current_user.is_staff if current_user.is_authenticated else False
    isNotSignedIn = not current_user.is_authenticated

    return render(request, "pages/delBook.html", {'isAdmin': isAdmin, 'isNotSignedIn': isNotSignedIn})




def bookDetails(request, id):
    return render(request, "pages/bookDetails.html", {'Book': Book.objects.get(id=id)})




def borrowedBooksPage(request):
    return render(request, 'pages/view_borrowed_book.html',{'books':Book.objects.filter(Borrow = User.objects.get(username=request.user))})




def borrow(request, id):
    book = Book.objects.get(id=id)
    book.Borrow = request.user
    book.availability = False
    book.save()
    return redirect("../books")

def unBorrow(request, id):
    book = Book.objects.get(id=id)
    book.Borrow = None
    book.availability = True
    book.save()    
    return redirect("../../books/borrowedBooks")



def search_results(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.method == 'POST':
            book = request.POST.get('book')
            Queryset = Book.objects.filter(name__icontains = book)
            currentUser = request.user
            
            isAdmin = currentUser.is_staff if currentUser.is_authenticated else False

            print(Queryset)
            if len(Queryset) > 0 and len(book) > 0:
                Data = []
                for pos in Queryset:
                    dic = {
                        "title": pos.name,
                        "author": pos.author,
                        "category": pos.category.name,
                        "image": pos.image.url,
                        "id" : pos.id
                    }
                    Data.append(dic)
                res = Data
            else:
                res = "no Books Found"
            return JsonResponse({'data': res , "isAdmin": isAdmin} ) 
    return JsonResponse({})