from django.shortcuts import redirect, render_to_response
from django.core.urlresolvers import reverse
from titan import settings
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf

def index(request):
    return redirect(settings.LOGIN_URL)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/me/")
    else:
        form = UserCreationForm()
    c = {'form': form}
    c.update(csrf(request))
    return render_to_response("registration/register.html", c)
