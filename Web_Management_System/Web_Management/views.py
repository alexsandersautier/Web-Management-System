from django.shortcuts import render,HttpResponse, redirect
from .models import Books, Movies
from .forms import BooksForm, MoviesForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

@login_required
def home(request):
    data = {
        'data': Books.objects.all()
    }
    return render(request, 'web_management/home.html', context=data)
@login_required
def new_book(request):
    if request.method=='POST':
        book_form = BooksForm(request.POST)
        if book_form.is_valid():
            book_form.save()
        return redirect('home')    

    book_form = BooksForm()
    form = {
        'form': book_form
    }
    return render(request, 'web_management/new_book.html', context=form)
@login_required
def book_registed(request,id):
    data = {
        'data': Books.objects.get(pk=id)
    }
    return render(request, 'web_management/book_registed.html', data)
@login_required
def edit_register(request,id):
    book = Books.objects.get(pk=id)
    if request.method == 'GET':
        form = BooksForm(instance=book)
        return render(request, 'web_management/new_book.html', {'form': form})
    else:
        form = BooksForm(request.POST,instance=book)    
        if form.is_valid():
            form.save()
        return redirect('home')
@login_required
def delete(request,id):
    book = Books.objects.get(pk=id)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    return render(request, 'web_management/confirm_delete.html', {"item":book})

#movies
@login_required
def movie(request):
    data = {
        'data': Movies.objects.all()
    }
    return render(request, 'wmovies/home.html', context=data)
@login_required
def new_movie(request):
    if request.method=='POST':
        movie_form = MoviesForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
        return redirect('movie')    

    movies_form = MoviesForm()
    form = {
        'form': movies_form
    }
    return render(request, 'wmovies/new_movie.html', context=form)    
@login_required
def movie_registed(request,id):
    data = {
        'data': Movies.objects.get(pk=id)
    }
    return render(request, 'wmovies/movie_registed.html', data)
@login_required
def edit_movie(request,id):
    movie = Movies.objects.get(pk=id)
    if request.method == 'GET':
        form = MoviesForm(instance=movie)
        return render(request, 'wmovies/new_movie.html', {'form': form})
    else:
        form = MoviesForm(request.POST,instance=movie)    
        if form.is_valid():
            form.save()
        return redirect('movie') 
@login_required
def delete_movie(request,id):
    movie = Movies.objects.get(pk=id)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie')
    return render(request, 'wmovies/confirm_delete.html', {"item":movie})