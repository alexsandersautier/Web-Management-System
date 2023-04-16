from django.forms import ModelForm
from .models import Books, Movies

class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

class MoviesForm(ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'