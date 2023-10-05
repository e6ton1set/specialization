from django.shortcuts import render
from myapp2.views import get_eagle_or_tails, get_side_cube, get_rnd_num
from myapp4.forms import ChoiceForm


def choice_games_form(request):
    if request.method == "POST":
        form = ChoiceForm(request.POST)
        if form.is_valid():
            count = int(form.cleaned_data["count"])
            match form.cleaned_data["choice_game"]:
                case "form_eagle":
                    return get_eagle_or_tails(request, count)
                case "form_cube":
                    return get_side_cube(request, count)
                case "form_rnd_num":
                    return get_rnd_num(request, count)
    else:
        form = ChoiceForm()
    return render(request, "myapp4/choice_games_form.html", {"form": form})
