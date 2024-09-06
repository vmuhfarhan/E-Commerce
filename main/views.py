from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'namaAplikasi' : '2306231422',
        'nama': 'Muhammad Farhan Ramadhan',
        'kelas': 'PBP A'
    }

    return render(request, "main.html", context)
