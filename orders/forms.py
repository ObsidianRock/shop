from django import forms
from .models import Order

from localflavor.gb.forms import GBPostcodeField


class OrderCreateForm(forms.ModelForm):
    postal_code = GBPostcodeField()

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']