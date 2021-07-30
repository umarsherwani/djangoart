from django.contrib.auth import login, authenticate
from .forms import PostForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('base.html')
    else:
        form = PostForm()
    return render(request, 'signup.html', {'form': form})