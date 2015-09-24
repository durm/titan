from django.shortcuts import redirect, render_to_response
from django.core.urlresolvers import reverse
from titan import settings
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login
from units.views import mylist

def index(request):
    return redirect(settings.LOGIN_URL)

def register(request):
    if request.user.is_authenticated():
        return redirect(reverse(mylist))
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, new_user)
            return redirect(reverse(mylist))
    else:
        form = UserCreationForm()
    c = {'form': form}
    c.update(csrf(request))
    return render_to_response("registration/register.html", c)