from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ShoesEntryForm
from main.models import Sepatu
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    shoes_entries = Sepatu.objects.all()

    context = {
        'namaAplikasi' : '2306231422',
        'nama': 'Muhammad Farhan Ramadhan',
        'kelas': 'PBP A',
        'shoes_entries': shoes_entries
    }

    return render(request, "main.html", context)

def create_shoes_entry(request):
    form = ShoesEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_shoes_entry.html", context)

def show_xml(request):
    data = Sepatu.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Sepatu.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Sepatu.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Sepatu.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
