from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now login.')
            return redirect('login')
        else:
            messages.error(request, 'Error: Please correct the form.')
    else:
        form = UserCreationForm()
    return render(request, 'complaints/register.html', {'form': form})

def complaint_list(request):
    return render(request, 'complaints/complaint_list.html')