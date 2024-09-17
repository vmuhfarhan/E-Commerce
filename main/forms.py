from django.forms import ModelForm
from main.models import Sepatu

class ShoesEntryForm(ModelForm):
    class Meta:
        model = Sepatu
        fields = ["name", "description", "price"]