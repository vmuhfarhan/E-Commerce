from django.forms import ModelForm
from main.models import ShoesEntry

class ShoesEntryForm(ModelForm):
    class Meta:
        model = ShoesEntry
        fields = ["name", "description", "price"]