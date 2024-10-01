import datetime
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from main.forms import ShoesEntryForm
from main.models import ShoesEntry
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def show_xml(request):
    data = ShoesEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ShoesEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ShoesEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ShoesEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login')
def show_main(request):
    shoes_entries = ShoesEntry.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'class': 'PBP A',
        'npm' : '2306231422',
        'shoes_entries': shoes_entries,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_shoes_entry(request):
    form = ShoesEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        shoes_entry = form.save(commit=False)
        shoes_entry.user = request.user
        shoes_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_shoes_entry.html", context)

def edit_shoes(request, id):
    shoes = ShoesEntry.objects.get(pk = id)
    form = ShoesEntryForm(request.POST or None, instance=shoes)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_shoes.html", context)

def delete_shoes(request, id):
    shoes = ShoesEntry.objects.get(pk = id)
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
    context = {'form':form}
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