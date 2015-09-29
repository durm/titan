from django.shortcuts import render_to_response, redirect
from units.models import Unit, get_item_types, Item
from django.template.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required
def save(request, num=None):
    if request.method == 'GET':
        c = {"unit": Unit.objects.get(id=int(num)) if num is not None else None}
        c.update(csrf(request))
        return render_to_response("save.html", c, context_instance=RequestContext(request))
    elif request.method == 'POST':
        if "unit_id" in request.POST:
            unit = Unit.objects.get(id=int(request.POST["unit_id"]))
            unit.name = request.POST["name"]
            unit.desc = request.POST["desc"]
            unit.updated_by = request.user
        else:
            unit = Unit(name=request.POST.get("name"), desc=request.POST.get("desc"), created_by=request.user, updated_by=request.user)
        unit.save()
        return redirect(reverse(page, kwargs={"num": int(unit.id)}))

@login_required    
def page(request, num=None):
    unit = Unit.objects.get(id=int(num))
    if request.method == 'GET':
        items = {}
        for item in Item.objects.filter(unit=unit):
            if item.item_type in items:
                items[item.item_type].append(item)
            else:
                items[item.item_type] = [item]
        item_types = get_item_types()
        c = {
            "unit": unit,
            "item_types": item_types,
            "item_types_dict": dict(item_types),
            "items": items
        }
        c.update(csrf(request))
        return render_to_response("unit.html", c, context_instance=RequestContext(request))
    elif request.method == 'POST':
        item = Item(content=request.POST.get("content"), item_type=request.POST.get("item_type"), unit=unit, created_by=request.user, updated_by=request.user)
        item.save()
    elif request.method == "DELETE":
        items = Item.objects.filter(unit=unit, id__in=map(int, request.DELETE["item"]))
        items.delete()
    return redirect(reverse(page, kwargs={"num": int(unit.id)}))

@login_required    
def mylist(request):
    mylist = Unit.objects.filter(created_by=request.user)
    return render_to_response("mylist.html", {"mylist": mylist}, context_instance=RequestContext(request))
