from django.contrib import admin
from django.urls import path
from Web_Management import views
from users import views as users_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', users_views.new_user,name='new_user'),
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', users_views.logout_view, name='logout'),

    path('home/', views.home, name='home'),
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
