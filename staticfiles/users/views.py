from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('login')

def new_user(request):
    if request.method == 'POST':
        form  = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'User {user} resgited success!')
            return redirect('login')
    else:
        form  = UserRegisterForm()        
    return render(request,'users/register.html', {'form': form})