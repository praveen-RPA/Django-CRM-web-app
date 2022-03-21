from django.forms import ModelForm
from .models import *

class OrderForm(ModelForm):
    class Meta:
        #model name - Order
        model=Order
        fields='__all__'