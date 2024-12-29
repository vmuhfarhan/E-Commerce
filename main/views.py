#views.py

import datetime
import json
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

#4=
@login_required(login_url='/login')
def show_main(request):
    context = {
        'name': request.user.username, #Menampilkan username user di halaman utama
        'class': 'PBP A',
        'npm': '2306231422',
        'last_login': request.COOKIES.get('last_login', ''), #Menampilkan last login user di halaman utama
    }
    return render(request, "main.html", context)
#=

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

#5=
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
#=

#4=
# Form Buat Register
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

# Form Buat Login
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

# Form Buat Logout
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
#=

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


##########
import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from main.models import ShoesEntry
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            data = request.POST

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return JsonResponse({
                "status": False,
                "message": "Username dan password harus diisi."
            }, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({
                "status": False,
                "message": "Username sudah digunakan."
            }, status=400)

        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return JsonResponse({
                "status": True,
                "message": "Register sukses!"
            }, status=200)
        except Exception as e:
            return JsonResponse({
                "status": False,
                "message": str(e)
            }, status=500)

    return JsonResponse({
        "status": False,
        "message": "Invalid request method."
    }, status=405)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            data = request.POST

        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return JsonResponse({
                    "status": True,
                    "message": "Login sukses!",
                    "username": user.username,
                }, status=200)
            else:
                return JsonResponse({
                    "status": False,
                    "message": "Akun dinonaktifkan."
                }, status=401)
        else:
            return JsonResponse({
                "status": False,
                "message": "Username atau password salah."
            }, status=401)

    return JsonResponse({
        "status": False,
        "message": "Invalid request method."
    }, status=405)

@csrf_exempt
def logout(request):
    username = request.user.username
    try:
        auth_logout(request)
        return JsonResponse({
            "status": True,
            "message": "Logout berhasil!",
            "username": username
        }, status=200)
    except Exception:
        return JsonResponse({
            "status": False,
            "message": "Logout gagal."
        }, status=401)

@csrf_exempt
@login_required(login_url='/login')
@require_POST
def create_shoes_flutter(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        data = request.POST

    try:
        name = data.get('name')
        price = data.get('price')
        description = data.get('description')

        if not name or not price or not description:
            return JsonResponse({
                "status": "error",
                "message": "Semua field harus diisi"
            }, status=400)

        try:
            price = int(price)
        except ValueError:
            return JsonResponse({
                "status": "error",
                "message": "Harga harus berupa angka"
            }, status=400)

        new_shoes = ShoesEntry.objects.create(
            user=request.user,
            name=name,
            description=description,
            price=price
        )
        new_shoes.save()

        return JsonResponse({
            "status": "success",
            "message": "Item berhasil ditambahkan!"
        }, status=201)
    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=500)

@csrf_exempt
@login_required(login_url='/login')
@require_POST
def edit_shoes_flutter(request, id):
    try:
        shoes = ShoesEntry.objects.get(pk=id, user=request.user)
    except ShoesEntry.DoesNotExist:
        return JsonResponse({
            "status": "error",
            "message": "Item tidak ditemukan."
        }, status=404)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        data = request.POST

    try:
        shoes.name = data.get('name', shoes.name)
        shoes.description = data.get('description', shoes.description)
        price = data.get('price')
        if price:
            shoes.price = int(price)
        shoes.save()

        return JsonResponse({
            "status": "success",
            "message": "Item berhasil diperbarui!"
        }, status=200)
    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=400)

@csrf_exempt
@login_required(login_url='/login')
@require_POST
def delete_shoes_flutter(request, id):
    try:
        shoes = ShoesEntry.objects.get(pk=id, user=request.user)
        shoes.delete()
        return JsonResponse({
            "status": "success",
            "message": "Item berhasil dihapus!"
        }, status=200)
    except ShoesEntry.DoesNotExist:
        return JsonResponse({
            "status": "error",
            "message": "Item tidak ditemukan."
        }, status=404)
    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=500)

@login_required(login_url='/login')
def get_user_shoes(request):
    if request.method == 'GET':
        shoes = ShoesEntry.objects.filter(user=request.user)
        return JsonResponse({
            "shoes": [
                {
                    "id": str(shoe.id),
                    "name": shoe.name,
                    "price": shoe.price,
                    "description": shoe.description,
                    "time": shoe.time.strftime('%Y-%m-%d')
                }
                for shoe in shoes
            ]
        }, status=200)
    return JsonResponse({
        "status": "error",
        "message": "Invalid request method."
    }, status=405)