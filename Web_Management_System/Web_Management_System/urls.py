"""Web_Management_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Web_Management import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('new_book/', views.new_book, name='new_book'),
    path('new_book/<int:id>', views.edit_register, name='edit'),
    path('delete_book/<int:id>', views.delete, name='delete'),
    path('book_registed/<int:id>', views.book_registed, name='book_registed'),

    path('movie/', views.movie, name='movie'),
    path('movie_registed/<int:id>', views.movie_registed, name='movie_registed'),
    path('new_movie/', views.new_movie, name='new_movie'),
    path('new_movie/<int:id>', views.edit_movie, name='edit_movie'),
    path('delete_movie/<int:id>', views.delete_movie, name='delete_movie'),
]
