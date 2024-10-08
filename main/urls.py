from django.urls import path
from main.views import show_main, create_shoes_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user, edit_shoes, delete_shoes
from main.views import add_shoes_entry_ajax, edit_shoes_ajax, delete_shoes_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-shoes-entry/', create_shoes_entry, name='create_shoes_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-shoes/<int:id>/', edit_shoes, name='edit_shoes'),
    path('delete-shoes/<int:id>/', delete_shoes, name='delete_shoes'),
    path('create-shoes-entry-ajax/', add_shoes_entry_ajax, name='add_shoes_entry_ajax'),
    path('edit-shoes-ajax/<uuid:id>/', edit_shoes_ajax, name='edit_shoes_ajax'),
    path('delete-shoes-ajax/<uuid:id>/', delete_shoes_ajax, name='delete_shoes_ajax'),
]