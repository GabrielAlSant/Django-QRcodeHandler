from django.shortcuts import render
from .models import Produto

def home(request):
    
    produtos = {
        'produtos': Produto.objects.all() 
    }
    return render(request, 'produtos/home.html', produtos)

def produtos(request):
    novo_produto = Produto()
    novo_produto.nome = request.POST.get("nome")
    novo_produto.preco = request.POST.get("preco")
    novo_produto.img = request.POST.get("img")
    novo_produto.save()
    produtos = {
        'produtos': Produto.objects.all() 
    }
    return render(request, 'produtos/home.html', produtos)

def excluirproduto(request, id ):
  
  produto = Produto.objects.get(id=id)
  produto.delete()

  produtos = {
        'produtos': Produto.objects.all() 
    }

  return render(request, 'produtos/home.html', produtos)

def filtroproduto(request): 
   name = request.POST.get("nome")
  
   produtos = {
        'produtos':  Produto.objects.filter(nome = str(name)).values()
    }
   
   return render(request, 'produtos/home.html', produtos)

