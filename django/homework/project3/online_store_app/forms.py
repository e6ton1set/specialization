from django.core.files.storage import FileSystemStorage
from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=20,
                           widget=forms.TextInput(
                               attrs={"placeholder": "Наименование"}),
                           label="")
    description = forms.CharField(max_length=200,
                                  widget=forms.Textarea(
                                      attrs={
                                          "class": "input-text long_input",
                                          "placeholder": "Описание файла"}),
                                  label="")
    price = forms.DecimalField(max_digits=8,
                               decimal_places=2,
                               widget=forms.NumberInput(
                                   attrs={"placeholder": "Цена"}),
                               label="")
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": "Количество"}),
                                label="")
    image = forms.ImageField(required=False,
                             widget=forms.ClearableFileInput(
                                 attrs={"class": "input-file",
                                        "placeholder": "Изображение"}),
                             label="")
