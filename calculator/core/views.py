from django.shortcuts import render
from .forms import CalcForm


def index(request):
    result = 0
    if request.method == "POST":
        form = CalcForm(request.POST)
        if form.is_valid:
            result = eval(form["equation"].value())
    else:
        form = CalcForm()
    context = {"form": form, "result": result}
    return render(request, "core/index.html", context)
