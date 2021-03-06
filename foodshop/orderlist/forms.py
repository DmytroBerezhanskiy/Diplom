from django import forms

PRODUCT_COUNT_CHOICES = [(i, str(i)) for i in range(1, 21)]


class OrderListAddProductForm(forms.Form):
    count = forms.TypedChoiceField(choices=PRODUCT_COUNT_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
