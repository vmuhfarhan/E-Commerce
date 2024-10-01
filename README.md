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
    ![Screenshot (447)](https://github.com/user-attachments/assets/76916160-db87-472b-95f7-085633013667)

    ### 2. Semua Data Sepatu dalam Format JSON
    ![Screenshot (448)](https://github.com/user-attachments/assets/975da0ea-6dc7-4d60-bd66-86f9f12cea73)

    ### 3. Data Sepatu Berdasarkan ID dalam Format XML
    ![Screenshot (449)](https://github.com/user-attachments/assets/685a7adf-af33-4f27-9442-92c7367a8a44)

    ### 4. Data Sepatu Berdasarkan ID dalam Format JSON
    ![Screenshot (450)](https://github.com/user-attachments/assets/691b8fe8-cf48-487a-9f59-19c7099efad1)

Tugas 4
1. Apa perbedaan antara HttpResponseRedirect() dan redirect()?
    - HttpResponseRedirect() adalah class Django yang digunakan untuk mengarahkan (redirect) pengguna ke URL tertentu. HttpResponseRedirect() memerlukan argumen berupa URL yang dituju. Ini adalah respons HTTP dengan status code 302 yang mengarahkan browser untuk menuju URL baru.
    - redirect() adalah shortcut yang lebih praktis untuk melakukan pengalihan (redirect) dalam Django. Selain URL, redirect() dapat menerima nama view, bahkan objek model sebagai argumen. Fungsi ini secara otomatis menangani detail pengalihan dan mempermudah penggunaannya.

2. Jelaskan cara kerja penghubungan model Product dengan User!
    Dalam Django, penghubungan antara model Product dan User dilakukan dengan menggunakan relasi ForeignKey. Relasi ini menghubungkan setiap instance dari model Product dengan satu instance dari model User, di mana produk tersebut dimiliki oleh pengguna tertentu.

    ` models.py `
    class Sepatu(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE) --> Penggunaan ForeignKey
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        name = models.CharField(max_length=255)
        description = models.TextField()
        price = models.IntegerField()

3.  Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

    Authentication (Autentikasi) merupakan proses untuk memverifikasi identitas pengguna. Pengguna diminta untuk memasukkan kredensial seperti username dan password, dan jika sesuai dengan data di database, pengguna dianggap berhasil terotentikasi. Autentikasi bertujuan untuk memastikan siapa pengguna tersebut. 
    
    Authorization (Otorisasi) merupakan proses menentukan apa yang boleh dilakukan oleh pengguna yang sudah terautentikasi. Ini mengacu pada izin atau hak akses pengguna terhadap sumber daya atau fitur dalam aplikasi. Otorisasi menentukan apakah pengguna memiliki hak untuk melakukan tindakan tertentu, seperti mengakses halaman admin atau mengedit data.

    Saat pengguna login, proses yang dilakukan adalah autentikasi. Django memverifikasi kredensial yang diberikan pengguna. Jika valid, pengguna akan dianggap terotentikasi. Setelah berhasil login, proses otorisasi akan memastikan bahwa pengguna hanya dapat mengakses halaman atau melakukan tindakan yang sesuai dengan izin mereka.

    Implementasi Authentication:
    `views.py`
    from django.contrib.auth import authenticate, login

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

    Implementasi Authorization:
    `views.py`
    from django.contrib.auth.decorators import login_required

    @login_required(login_url='/login')
    def show_main(request):
        shoes_entries = Sepatu.objects.filter(user=request.user)

        context = {
            'namaAplikasi' : 'E-Commerce',
            'nama': request.user.username,
            'kelas': 'PBP A',
            'shoes_entries': shoes_entries,
            'last_login': request.COOKIES['last_login'],
        }

        return render(request, "main.html", context)

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

    Cara Django mengingat pengguna yang telah login adalah Django menggunakan sistem session untuk mengingat pengguna yang telah login. Setelah pengguna login, Django menyimpan session ID di server dan mengirimkan cookies ke browser pengguna yang berisi session ID tersebut. Setiap kali pengguna mengirimkan request berikutnya, cookies tersebut dikirimkan kembali ke server untuk mengidentifikasi pengguna.

    Adapun kegunaan lain dari cookies adalah Cookies sering digunakan untuk menyimpan pengaturan preferensi seperti bahasa atau tema. Cookies bisa melacak aktivitas pengguna, seperti barang yang ditambahkan ke keranjang belanja di e-commerce. Cookies dapat digunakan untuk mengingat pengguna sehingga pengguna tidak perlu login setiap kali mengakses aplikasi.

    Tidak semua cookies aman, terutama jika tidak dikelola dengan benar. Cookies yang berisi informasi sensitif dapat menjadi target serangan seperti pencurian identitas atau session hijacking.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

    1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

        `views.py`
        from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
        from django.contrib.auth import authenticate, login, logout
        from django.contrib.auth.decorators import login_required

        **Buat view untuk menangani registrasi pengguna baru menggunakan UserCreationForm dari Django. Setelah pengguna mengirimkan form pendaftaran dan berhasil diverifikasi, login otomatis dilakukan atau pengguna diarahkan ke halaman login.

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

        ** Buat view untuk login menggunakan AuthenticationForm bawaan Django. Pastikan pengguna yang login berhasil diarahkan ke halaman utama atau halaman tujuan setelah autentikasi.

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

        ** Gunakan view logout bawaan Django untuk menangani proses logout dan membersihkan session pengguna. Setelah logout, arahkan pengguna ke halaman login atau halaman utama.

        def logout_user(request):
            logout(request)
            response = HttpResponseRedirect(reverse('main:login'))
            response.delete_cookie('last_login')
            return response

    2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

    3. Menghubungkan model Product dengan User.
        Di model Product, tambahkan atribut owner yang merupakan ForeignKey ke model User. Ini memungkinkan setiap produk memiliki satu pemilik yang merupakan pengguna terdaftar.

        `models.py`
        from django.contrib.auth.models import User

        class Sepatu(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)
            id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
            name = models.CharField(max_length=255)
            description = models.TextField()
            price = models.IntegerField()

        Saat menambahkan data ke Product, pastikan bahwa produk tersebut memiliki hubungan dengan pengguna yang sedang login. Ketika pengguna membuat produk baru, relasi dengan pengguna disimpan di atribut owner.

        `views.py`
        def create_shoes_entry(request):
            form = ShoesEntryForm(request.POST or None)

            if form.is_valid() and request.method == "POST":
                shoes_entries = form.save(commit=False)
                shoes_entries.user = request.user
                shoes_entries.save()
                return redirect('main:show_main')

            context = {'form': form}
            return render(request, "create_shoes_entry.html", context)

    4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

        Implementasikan cookies untuk menyimpan data seperti waktu last login. Di view login, setelah pengguna berhasil login, simpan waktu login ke cookies menggunakan set_cookie().
        `views.py`
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

        `main.html`
        <h5>Welcome! </h5>
        <p>{{nama}}</p>

        <h5>Sesi terakhir login: {{ last_login }}</h5>    

Tugas 5
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
    
    Prioritas CSS atau spesifisitas adalah cara browser menentukan aturan CSS mana yang diterapkan pada elemen HTML jika ada beberapa selector yang sesuai. Urutan prioritasnya adalah sebagai berikut:
    1. Inline Styles: Gaya yang diterapkan langsung pada elemen menggunakan atribut style. Contoh: <div style="color: red;">.
    2. IDs: Selector yang menggunakan ID. Contoh: #myId.
    3. Classes, Attributes, dan Pseudo-classes: Selector yang menggunakan kelas, atribut, atau pseudo-classes. Contoh: .myClass, [type="text"], dan :hover.
    4. Element (Tag) dan Pseudo-elements: Selector yang menggunakan elemen HTML atau pseudo-elements. Contoh: div, p, dan ::before.
    
    Jika beberapa selector memiliki spesifisitas yang sama, urutan terakhir yang diterapkan akan digunakan, berdasarkan urutan kemunculan di dalam CSS (last rule wins).

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

    Responsive design adalah pendekatan dalam pengembangan web yang memastikan bahwa situs web dapat berfungsi dengan baik di berbagai perangkat dan ukuran layar, seperti desktop, tablet, dan ponsel pintar. Konsep ini penting karena memberikan pengalaman yang konsisten dan nyaman di semua perangkat. Selain itu, responsive design memudahkan pencarian karena Google lebih menyukai situs web yang responsif dalam hasil pencariannya. Responsive design juga memastikan konten dapat diakses oleh lebih banyak pengguna.

    Contoh yang sudah responsive design : Tokopedia
    Contoh yang belum responsive design : Pacil Web Service (PWS)

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

    Margin: Ruang di luar elemen. Margin memisahkan elemen dari elemen lain. Dapat diatur menggunakan CSS: margin: 10px;.
    Border: Garis yang mengelilingi elemen. Border dapat memiliki berbagai gaya, lebar, dan warna. Contoh: border: 1px solid black;.
    Padding: Ruang di dalam elemen, antara konten dan border. Padding membuat konten tidak langsung menyentuh border. Contoh: padding: 10px;.

    contoh implementasi:
    .box {
    margin: 20px;    ---> Ruang luar
    border: 2px solid black;  ---> Garis border
    padding: 15px;   ---> Ruang dalam
    }

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

    Flexbox adalah model layout CSS yang digunakan untuk mendistribusikan ruang di antara item dalam kontainer. Dengan flexbox, Anda dapat dengan mudah mengatur item dalam satu dimensi (baik horizontal maupun vertikal). Kegunaannya meliputi penataan elemen dalam baris atau kolom serta pengaturan ruang antar elemen secara otomatis.

    contoh implementasi:
    .container {
    display: flex;
    justify-content: space-between; /* Mengatur jarak antar item */
    }

    Grid Layout: Grid layout adalah sistem layout dua dimensi yang memungkinkan Anda untuk membuat tata letak yang lebih kompleks. Anda dapat mengatur elemen dalam baris dan kolom secara bersamaan. Kegunaannya meliputi pembuatan tata letak yang lebih terstruktur dan pengaturan elemen dalam area grid dengan lebih fleksibel.

    contoh implementasi:
    .grid-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* Membagi menjadi 3 kolom */
    gap: 10px; /* Jarak antar elemen */
    }

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

    1. Implementasikan fungsi untuk menghapus dan mengedit product.

        `views.py`
        **fungsi untuk meng-edit product
        def edit_shoes(request, id):
            shoes = ShoesEntry.objects.get(pk = id)
            form = ShoesEntryForm(request.POST or None, instance=shoes)

            if form.is_valid() and request.method == "POST":
                form.save()
                return HttpResponseRedirect(reverse('main:show_main'))

            context = {'form': form}
            return render(request, "edit_shoes.html", context)

        **fungsi untuk menghapus product
        def delete_shoes(request, id):
            shoes = ShoesEntry.objects.get(pk = id)
            shoes.delete()
            return HttpResponseRedirect(reverse('main:show_main'))
    
    2. Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:

        `login.html`
        {% extends 'base.html' %}

        {% block content %}
        <div class="max-w-md mx-auto bg-white shadow-md rounded-lg p-6">
            <h1 class="text-2xl font-bold mb-6">Login</h1>
            <form method="POST">
                {% csrf_token %}
                {% for field in form %}
                    <div class="mb-4">
                        <label for="{{ field.id_for_label }}" class="block text-gray-700 font-bold mb-2">{{ field.label }}</label>
                        {{ field }}
                    </div>
                {% endfor %}
                <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Login</button>
            </form>
            <p class="mt-4">Don't have an account? <a href="{% url 'main:register' %}" class="text-blue-500 hover:underline">Register here</a></p>
        </div>
        {% endblock %}


        `register.html`
        {% extends 'base.html' %}

        {% block content %}
        <div class="max-w-md mx-auto bg-white shadow-md rounded-lg p-6">
            <h1 class="text-2xl font-bold mb-6">Register</h1>
            <form method="POST">
                {% csrf_token %}
                {% for field in form %}
                    <div class="mb-4">
                        <label for="{{ field.id_for_label }}" class="block text-gray-700 font-bold mb-2">{{ field.label }}</label>
                        {{ field }}
                        {% if field.help_text %}
                            <p class="text-sm text-gray-500 mt-1">{{ field.help_text }}</p>
                        {% endif %}
                    </div>
                {% endfor %}
                <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Register</button>
            </form>
            <p class="mt-4">Already have an account? <a href="{% url 'main:login' %}" class="text-blue-500 hover:underline">Login here</a></p>
        </div>
        {% endblock %}


        `create_shoes_entry.html`
        {% extends 'base.html' %}

        {% block content %}
        <div class="max-w-md mx-auto bg-white shadow-md rounded-lg p-6">
            <h1 class="text-2xl font-bold mb-6">Create New Shoes Entry</h1>
            <form method="POST">
                {% csrf_token %}
                {% for field in form %}
                    <div class="mb-4">
                        <label for="{{ field.id_for_label }}" class="block text-gray-700 font-bold mb-2">{{ field.label }}</label>
                        {{ field }}
                    </div>
                {% endfor %}
                <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Create</button>
            </form>
        </div>
        {% endblock %}


        `card_shoes.html`
        <div class="bg-white shadow-md rounded-lg p-6 mb-4">
            <h3 class="text-xl font-bold mb-2">{{ shoes.name }}</h3>
            <p class="text-gray-600 mb-2">{{ shoes.description }}</p>
            <p class="text-lg font-semibold mb-4">${{ shoes.price }}</p>
            <div class="flex justify-between">
                <a href="{% url 'main:edit_shoes' shoes.id %}" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Edit</a>
                <a href="{% url 'main:delete_shoes' shoes.id %}" class="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600">Delete</a>
            </div>
            </div>


        `main.html`
        {% extends 'base.html' %}

        {% block content %}
            {% include 'card_info.html' %}
            
            <h2 class="text-2xl font-bold mb-4">My Shoes Collection</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {% for shoes in shoes_entries %}
                    {% include 'card_shoes.html' with shoes=shoes %}
                {% empty %}
                    <p class="col-span-full text-center text-gray-500">No shoes entries yet. Add some!</p>
                {% endfor %}
            </div>
            
            <a href="{% url 'main:create_shoes_entry' %}" class="mt-6 inline-block bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">Add New Shoes</a>
        {% endblock %}


        `edit_shoes.html`
        {% extends 'base.html' %}

        {% block content %}
        <div class="max-w-md mx-auto bg-white shadow-md rounded-lg p-6">
            <h1 class="text-2xl font-bold mb-6">Edit Shoes Entry</h1>
            <form method="POST">
                {% csrf_token %}
                {% for field in form %}
                    <div class="mb-4">
                        <label for="{{ field.id_for_label }}" class="block text-gray-700 font-bold mb-2">{{ field.label }}</label>
                        {{ field }}
                    </div>
                {% endfor %}
                <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Save Changes</button>
            </form>
        </div>
        {% endblock %}


        `base.html`
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{% block title %}E-Commerce{% endblock %}</title>
            {% load static %}
            <link rel="stylesheet" href="{% static 'css/global.css' %}">
            <script src="https://cdn.tailwindcss.com"></script>
        </head>
        <body class="bg-gray-100 min-h-screen flex flex-col">
            {% include 'navbar.html' %}
            <main class="flex-grow container mx-auto px-4 py-8">
                {% block content %}
                {% endblock %}
            </main>
            <footer class="bg-gray-800 text-white py-4">
                <div class="container mx-auto text-center">
                    &copy; 2024 E-Commerce. All rights reserved.
                </div>
            </footer>
        </body>
        </html>


        `navbar.html`
        <nav class="bg-gray-800 text-white">
            <div class="container mx-auto px-4">
                <div class="flex items-center justify-between h-16">
                    <a href="{% url 'main:show_main' %}" class="text-xl font-bold">E-Commerce</a>
                    
                    <!-- Hamburger button for mobile -->
                    <button id="mobile-menu-button" class="md:hidden focus:outline-none">
                        <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path>
                        </svg>
                    </button>
                    
                    <!-- Desktop menu -->
                    <div class="hidden md:flex space-x-4">
                        {% if user.is_authenticated %}
                            <span class="text-gray-300 mr-4">Welcome, {{ user.username }}</span>
                            <a href="{% url 'main:logout' %}" class="hover:text-gray-300">Logout</a>
                        {% else %}
                            <a href="{% url 'main:login' %}" class="hover:text-gray-300">Login</a>
                            <a href="{% url 'main:register' %}" class="hover:text-gray-300">Register</a>
                        {% endif %}
                    </div>
                </div>
                
                <!-- Mobile menu -->
                <div id="mobile-menu" class="hidden md:hidden mt-2">
                    {% if user.is_authenticated %}
                        <div class="text-gray-300 py-2">Welcome, {{ user.username }}</div>
                        <a href="{% url 'main:logout' %}" class="block py-2 hover:text-gray-300">Logout</a>
                    {% else %}
                        <a href="{% url 'main:login' %}" class="block py-2 hover:text-gray-300">Login</a>
                        <a href="{% url 'main:register' %}" class="block py-2 hover:text-gray-300">Register</a>
                    {% endif %}
                </div>
            </div>
        </nav>

        <script>
            document.getElementById('mobile-menu-button').addEventListener('click', function() {
                var menu = document.getElementById('mobile-menu');
                menu.classList.toggle('hidden');
            });
        </script>





