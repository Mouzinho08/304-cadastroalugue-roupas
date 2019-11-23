from django.shortcuts import render
from website.forms import PedidoForm

# Create your views here.


def produtos(request):
    return render(request, 'produtos.html')

def home(request):
    return render(request, "home.html")

def cadastro_pedido(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'formulario':form
    }
    return render(request, 'pedido.html',context)