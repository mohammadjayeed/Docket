from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CustomRegistrationForm
from django.contrib import messages

def registration(request):

    if request.method == 'POST':
        registration_form = CustomRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request,("Success, please login to continue"))
            return redirect('registration_todo')

    else:

        registration_form = CustomRegistrationForm()

    return render(request, 'registration.html', {'registration_form': registration_form})
