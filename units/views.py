from django.shortcuts import render_to_response

def read_unit(request):
    return render_to_response("create_unit.html", {})
