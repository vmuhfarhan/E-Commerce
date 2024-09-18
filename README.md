Nama : Muhammad Farhan Ramadhan
NPM : 2306231422
Kelas : PBP A (AFK)

Tugas 2
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    Step 1: Membuat setup virtual environment menggunakan Python Virtual Environment dengan command di Terminal `python -m venv env` atau `python -m virtualenv env`. Setelahnya, aktifkan virtual environment dengan command `env\Scripts\activate`.

    Step 2: Membuat project Django yang dijalankan di virtual environment dengan command (setelah venv diaktifkan) `django-admin startproject <nama_proyek>` (catatan: nama_proyek diisi, dalam konteks ini, sesuai nama directory, dalam konteks ini adalah `ecommerce`).

    Step 3: Membuat aplikasi Django dengan command `django-admin startapp <nama_proyek>` (catatan: nama_proyek diisi, dalam konteks ini, `main`) dan menambahkan `main`, localserver, dan PWS web deployment address di list `ALLOWED_HOST` di `setting.py`.

    Step 4: Membuat model aplikasi di `models.py` yang ada di aplikasi `main`, dengan memasukkan Class(es) yang dibutuhkan. Seperti contohnya, dalam aplikasi ini, memasukkan Class bernama `Sepatu` dengan berbagai atribut beserta Fields yang dibutuhkan.

    contoh: class Sepatu(models.Model):
        # Menampilkan 3 entri wajib dari class Sepatu yang diminta
        name = models.CharField(max_length=100)
        price = models.IntegerField()
        description = models.TextField()

    Step 5: Melakukan migrasi serta membuat dan menambah URL & View. Memulai migrasi setiap adanya perubahan models yang terjadi di `models.py` dengan command `python manage.py makemigrations` dan dilanjutkan dengan `python manage.py migrate`. Setelahnya, menambahkan URL di `urls.py` di aplikasi (konteks: `main`) dan di project (konteks: `ecommerce`) dengan menambahkan URL di kedua `urls.py` tersebut. URL tersebut akan dipakai untuk menampilkan request yang akan ditampilkan dari `views.py`. `views.py` dapat ditambahkan method `show_main` untuk menampilkan berbagai atribut yang diinginkan dengan sekaligus `import render` dalam views.py yang akan ditampilkan di HTML (konteks: `main.html`).

    `Code Entry (urls.py di main)`
    ...
    from django.urls import path
    from main.views import show_main
 
    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'), # Setup for Django's main app
    ]
    ...

    `Code Entry (urls.py di project)`
    ...
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls), # Direct requests to Django admin interface
        path('', include('main.urls')), # Direct requests to main's urls.py
    ]
    ...

    `Code Entry (views.py)`
    ...
    from django import render

    #Create your views here
    def show_main(request):
        context = {
            'name' : 'Nike Air Max 97 Sean Wotherspoon',
            'price': 3350000,
            ...
        }
    
    #Render the request to the main.html as the given template with the context database to view
    return render(request, 'main.html', context)
    ...

    Step 6: Melakukan test server lewat localserver venv dan commit, deployment di PWS dan/atau Github. Jangan lupa untuk menambahkan URL deployment di `ALLOWED_HOSTS`.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

    Bagan : `Client Request -> urls.py -> views.py -> models.py -> views.py -> templates (HTML) -> Client Response`

    - urls.py: Menerima request dari client dan menentukan view yang akan dipanggil berdasarkan URL yang diambil.
    - views.py: Mengambil data dari model (jika diperlukan), memproses data (pada step ketiga), dan mengembalikan response (pada step kelima dan lewat HTML).
    - models.py: Berinteraksi dengan database untuk mengambil atau menyimpan data.
    - templates (HTML): Menampilkan data yang diproses oleh view dalam format HTML yang dikirim kembali ke client. Templates HTML dapat berupa aplikasi main atau yang lainnya.

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
    - Melacak perubahan sumber code selama pengembangan, baik dalam level local, global, maupun lewat aplikasi pihak ketiga secara online, seperti GitHub dan GitLab;
    - Memungkinkan kolaborasi bersama dalam satu project;
    - Memungkinkan adanya branch baru untuk perbaikan minor/major atau fitur baru tanpa mengganggu branch (kode) utama;
    - Memudahkan restore code jika terjadi kesalahan pada suatu stage/commit tertentu; dan
    - Memungkinkan merge, baik untuk pull maupun push request, perubahan dari berbagai branch.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    - Terdapat fitur bawaan seperti autentikasi, admin panel, Object-Relational Mapping (ORM), dan routing secara otomatis;
    - Dokumentasi lengkap, penggunaan luas, dan komunitas besar; 
    - Django menyediakan API yang juga mudah digunakan untuk operasi CRUD (Create, Read, Update, Delete); dan
    - Convention over Configuration (sehingga memudahkan pengguna baru untuk memahami alur pekerjaan aplikasi).

5. Mengapa model pada Django disebut sebagai ORM?
    Django menggunakan konsep OOP dan relasi untuk menghubungkan aplikasi dengan database secara relasional tanpa menggunakan SQL sehingga memudahkan pengembang untuk bekerja dengan menuliskan Object tanpa SQL. Django menyediakan API yang juga mudah digunakan untuk operasi CRUD (Create, Read, Update, Delete)


Tugas 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

    Data delivery penting dalam pengimplementasian platform karena memungkinkan pertukaran informasi antar komponen sistem, baik internal maupun eksternal, dengan cara yang terstruktur dan efisien. Dalam platform modern, berbagai layanan, modul, dan aplikasi harus berkomunikasi satu sama lain dan bertukar data untuk mendukung fungsionalitas yang lebih luas. Tanpa mekanisme data delivery yang efisien, sistem akan mengalami keterlambatan, kekurangan data, atau bahkan kegagalan dalam menjalankan operasi yang dibutuhkan. Selain itu, data delivery yang baik memastikan bahwa data dikirim dengan aman, tepat waktu, dan dalam format yang benar, mendukung kinerja platform dan pengalaman pengguna yang lancar.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

    Secara umum, JSON lebih disukai daripada XML dalam konteks web modern, terutama untuk API dan komunikasi data ringan. Namun, pemilihan antara keduanya tergantung pada kasus penggunaannya. XML lebih baik untuk dokumen yang kompleks dan membutuhkan metadata atau hierarki yang lebih kaya, serta untuk aplikasi yang menggunakan markup seperti dokumen atau format yang membutuhkan validasi yang kuat.

    Namun, JSON lebih populer karena beberapa alasan:
    - JSON lebih ringan dan sederhana, sehingga lebih mudah dibaca oleh manusia dan lebih cepat diproses oleh mesin.
    - JSON adalah format asli untuk JavaScript, sehingga lebih mudah diintegrasikan dalam aplikasi web.
    - JSON lebih hemat ruang dan lebih efisien saat dikirimkan melalui jaringan, membuatnya ideal untuk API yang memerlukan respon cepat.
    - Banyak framework modern seperti Django, Flask, dan Node.js secara default menggunakan JSON untuk komunikasi data.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

    Method is_valid() pada form Django berfungsi untuk memvalidasi data yang di-input oleh pengguna berdasarkan aturan yang telah ditentukan di form atau model terkait. Jika semua data valid sesuai kriteria, method ini akan mengembalikan nilai True, dan jika tidak, method akan mengembalikan nilai False serta menyediakan pesan kesalahan yang dapat ditampilkan kepada pengguna. 
    
    Kita membutuhkan method ini untuk:
    a. Memastikan bahwa data yang masuk sesuai dengan format atau tipe data yang diharapkan (misalnya, email yang valid, angka yang berada dalam rentang tertentu, dll)
    b. Memberikan pesan kesalahan yang informatif ketika ada data yang tidak valid, sehingga pengguna dapat memperbaikinya sebelum form disubmit ulang
    c. Memastikan bahwa hanya data yang valid yang masuk ke dalam sistem atau database

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

    csrf_token diperlukan untuk mencegah CSRF (Cross-Site Request Forgery), yaitu jenis serangan di mana penyerang memanfaatkan sesi pengguna yang sudah aktif untuk mengirim permintaan yang tidak sah ke server. Django secara otomatis menghasilkan csrf_token untuk setiap form yang aman, yang harus diverifikasi oleh server saat form tersebut di-submit.

    Jika kita tidak menambahkan csrf_token, maka form tersebut rentan terhadap serangan CSRF. Misalnya, penyerang bisa membuat pengguna yang tidak sadar untuk mengklik tautan atau mengirim form dari situs lain, yang dapat mengubah data penting atau menyebabkan tindakan berbahaya lainnya seperti mengubah pengaturan akun atau mentransfer dana.

    Tanpa csrf_token, penyerang dapat mengeksploitasi sesi pengguna yang aktif dengan mengirim permintaan palsu. Server tidak akan dapat memverifikasi apakah permintaan yang diterima sah atau berasal dari pengguna yang berwenang. Hal ini dapat mengakibatkan modifikasi data yang tidak sah, yang pada akhirnya membahayakan integritas dan keamanan platform serta pengguna.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    1. Membuat Input Form: Dimulai dengan membuat model Sepatu, lalu dilanjutkan dengan membuat form ShoesEntryForm yang merupakan form berbasis model. Setelah itu, saya membuat view untuk menampilkan form dan memproses input dari pengguna, serta menyimpan data ke database menggunakan method save().
    
    `Code Entry (forms.py)`
    from django.forms import ModelForm
    from main.models import Sepatu

    class ShoesEntryForm(ModelForm):
        class Meta:
            model = Sepatu
            fields = ["name", "description", "price"]

    `Code Entry (views.py)`
    def create_shoes_entry(request):
        form = ShoesEntryForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, "create_shoes_entry.html", context)

    2. Menambahkan 4 Fungsi Views untuk JSON dan XML: Saya kemudian menambahkan views baru (show_xml, show_json, show_xml_by_id, show_json_by_id) menggunakan serializers dari Django untuk mengubah objek model Sepatu menjadi format JSON dan XML. Untuk JSON dan XML berdasarkan ID, saya menggunakan filter berdasarkan primary key (id).

    `Code Entry (views.py)`
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

    3. Membuat Routing URL: Setelah views selesai, saya membuat rute di urls.py untuk menghubungkan setiap view ke URL yang sesuai. Ini memungkinkan saya mengakses data sepatu dalam format JSON/XML di URL seperti /json/, /xml/, serta /json/<id> dan /xml/<id>.

    `Code Entry (urls.py)`
    from django.urls import path
    from main.views import show_main, create_shoes_entry, show_xml, show_json, show_xml_by_id, show_json_by_id

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),  
        path('create-shoes-entry', create_shoes_entry, name='create_shoes_entry'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    ]

    4. Testing dengan Postman: Langkah terakhir adalah menguji URL yang dibuat menggunakan Postman untuk memastikan bahwa semua data dapat ditampilkan dalam format JSON dan XML, baik secara keseluruhan maupun berdasarkan ID.

    ## Hasil Akses URL di Postman

    ### 1. Semua Data Sepatu dalam Format XML
    ![XML All]("C:\Users\FARHAN\Downloads\github tugas 3\Screenshot (447).png")

    ### 2. Semua Data Sepatu dalam Format JSON
    ![JSON All]("C:\Users\FARHAN\Downloads\github tugas 3\Screenshot (448).png")

    ### 3. Data Sepatu Berdasarkan ID dalam Format XML
    ![XML by ID]("C:\Users\FARHAN\Downloads\github tugas 3\Screenshot (449).png")

    ### 4. Data Sepatu Berdasarkan ID dalam Format JSON
    ![JSON by ID]("C:\Users\FARHAN\Downloads\github tugas 3\Screenshot (450).png")

