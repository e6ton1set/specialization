from django import forms


class ChoiceForm(forms.Form):
    choice_game = forms.ChoiceField(choices=[("form_eagle", "Орёл или решка"),
                                             ("form_cube", "Подбросить кубик"),
                                             ("form_rnd_num", "Случайное число до 100")])
    count = forms.IntegerField(min_value=1,
                               max_value=64,
                               widget=forms.NumberInput(attrs={"class": "form_control"}))
