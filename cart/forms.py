from django import forms

class CartAddProductForm(forms.Form):
    Количество = forms.IntegerField(min_value=1, max_value=99)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput(attrs={"class":"input-number"}))

class CartAddOneProduct(forms.Form):
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput(attrs={"class":"input-number"}))


