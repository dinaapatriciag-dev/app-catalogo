from django.shortcuts import render,  get_object_or_404

from  .models import Obra 
 
def index(request):
    obras = Obra.objects.all()
    context ={
        "obras": obras,
    }

    return render(
        request,
        "catalogo/index.html",
        context
    )


def detalhes(request, id):
    obra_encontrada= Nome
    obra = get_object_or_404(obra, id=id)

    context = {
        # "obra" obra_encontrada,
    }

    return render(
        request,
        "catalogo/detalhes.html",
        context
    )