from django.shortcuts import redirect, render_to_response
from django.core.urlresolvers import reverse
from titan import settings

def index(request):
    return redirect(settings.LOGIN_URL)
