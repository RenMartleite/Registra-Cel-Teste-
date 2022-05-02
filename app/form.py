from django.forms import ModelForm
from app.models import Cels

# Create the form class.
class CelsForm(ModelForm):
    class Meta:
        model = Cels
        fields = ['modelo', 'marca', 'preco']