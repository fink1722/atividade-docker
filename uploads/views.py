from django.shortcuts import redirect, render

from .forms import ArquivoForm
from .models import Arquivo


def index(request):
    if request.method == "POST":
        form = ArquivoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ArquivoForm()
    return render(request, "uploads/index.html", {
        "form": form,
        "arquivos": Arquivo.objects.order_by("-id"),
    })
