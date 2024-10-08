import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from main.forms import ShoesEntryForm
from main.models import ShoesEntry
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_http_methods
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_main(request):
    context = {
        'name': request.user.username,
        'class': 'PBP A',
        'npm': '2306231422',
        'last_login': request.COOKIES.get('last_login', ''),
    }
    return render(request, "main.html", context)

@login_required(login_url='/login')
def show_xml(request):
    data = ShoesEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

@login_required(login_url='/login')
def show_json(request):
    data = ShoesEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login')
def show_xml_by_id(request, id):
    data = ShoesEntry.objects.filter(pk=id, user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

@login_required(login_url='/login')
def show_json_by_id(request, id):
    data = ShoesEntry.objects.filter(pk=id, user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login')
def create_shoes_entry(request):
    form = ShoesEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        shoes_entry = form.save(commit=False)
        shoes_entry.user = request.user
        shoes_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_shoes_entry.html", context)

@login_required(login_url='/login')
def edit_shoes(request, id):
    shoes = get_object_or_404(ShoesEntry, pk=id, user=request.user)
    form = ShoesEntryForm(request.POST or None, instance=shoes)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_shoes.html", context)

@login_required(login_url='/login')
def delete_shoes(request, id):
    shoes = get_object_or_404(ShoesEntry, pk=id, user=request.user)
    shoes.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')

    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def add_shoes_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    price = request.POST.get("price")
    user = request.user

    new_shoes = ShoesEntry(
        name=name, 
        description=description,
        price=price,
        user=user
    )
    new_shoes.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@login_required(login_url='/login')
@require_http_methods(["GET", "POST"])
def edit_shoes_ajax(request, id):
    shoes = get_object_or_404(ShoesEntry, pk=id, user=request.user)
    
    if request.method == 'GET':
        return JsonResponse({
            'name': shoes.name,
            'description': shoes.description,
            'price': shoes.price
        })
    
    elif request.method == 'POST':
        shoes.name = strip_tags(request.POST.get('name'))
        shoes.description = strip_tags(request.POST.get('description'))
        shoes.price = request.POST.get('price')
        shoes.save()
        return JsonResponse({'status': 'success'})

@csrf_exempt
@login_required(login_url='/login')
@require_POST
def delete_shoes_ajax(request, id):
    shoes = get_object_or_404(ShoesEntry, pk=id, user=request.user)
    shoes.delete()
    return JsonResponse({'status': 'success'})