from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import *
from .forms import *


#Read Method
class BooksList(View):
    def get(self,request):
        books = Book.objects.all()
        return render(request,"books.html",{'books':books})


#Create Method
class BookCreate(View):
    def get(self,request):
        form = BookForm()
        return render(request,"create_book.html",{'form':form})

    def post(self,request):
        form  = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books-list')
        return render(request, 'create_book.html', {'form': form})


class DeleteBook(View):
    def post(self,request,id):
        book = get_object_or_404(Book,id = id)
        book.delete()
        return redirect('books-list')

class BookUpdate(View):
    def get(self, request, id):
        book = get_object_or_404(Book, id = id)
        form = BookForm(instance=book)
        return render(request, 'update_book.html', {'form': form, 'book': book})

    def post(self, request, id):
        book = get_object_or_404(Book, id = id)
        form = BookForm(request.POST, instance=book)  
        if form.is_valid():
            form.save()
            return redirect('books-list')  
        return render(request, 'update_book.html', {'form': form, 'book': book})        
