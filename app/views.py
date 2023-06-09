from django.shortcuts import render, redirect
from .models import Produto
from .models import ProdutoCarrinho
from django.db.models import Sum
from django.http import HttpResponse
from io import BytesIO
from django.core.files.base import ContentFile
from django.shortcuts import render


def home(request):
    produtos = {
        'produtos': Produto.objects.all() ,
        'produtosCarrinho': ProdutoCarrinho.objects.all(),
        'valor' : ProdutoCarrinho.objects.aggregate(Sum('preco'))  
    }

    return render(request, 'produtos/home.html', produtos)



def produtos(request):
     novo_produto = Produto()
     novo_produto.nome = request.POST.get('nome')
     novo_produto.preco = request.POST.get('preco')
     novo_produto.url = request.POST.get('url')
     novo_produto.save()
     
    
     produtos = {
        'produtos': Produto.objects.all(), 
        'produtosCarrinho': ProdutoCarrinho.objects.all() 
    }
     return redirect('home')



 
def excluirproduto(request, id ):
  
  produto = Produto.objects.get(id=id)
  produto.delete()

  produtos = {
        'produtos': Produto.objects.all(),
        'produtosCarrinho': ProdutoCarrinho.objects.all() 
    }

  return redirect('home')


def filtroproduto(request): 
   name = request.POST.get("nome")
  
   produtos = {
        'produtos':  Produto.objects.filter(nome = str(name)).values(),
        'produtosCarrinho': ProdutoCarrinho.objects.all() 
    }
   
   return render(request, 'produtos/home.html', produtos)






def produtosCarrinho(request):
    novo_produto = ProdutoCarrinho()
    novo_produto.nome = request.POST.get("nome")
    novo_produto.preco = request.POST.get("preco")
    novo_produto.img = request.POST.get("img")
    novo_produto.save()


    produtos = {
        'produtos': Produto.objects.all(),
        'produtosCarrinho': ProdutoCarrinho.objects.all() 
    }
    return redirect('home')



def excluirprodutoCarrinho(request, id ):
  
  produto = ProdutoCarrinho.objects.get(id=id)
  produto.delete()

  produtos = {
        'produtos': Produto.objects.all(),
        'produtosCarrinho':  ProdutoCarrinho.objects.all()
    }
   
  return redirect('home')


def filtroprodutoCarrinho(request): 
   name = request.POST.get("nome")

   produtos = {
        'produtos': Produto.objects.all() ,
        'produtosCarrinho':  ProdutoCarrinho.objects.filter(nome = str(name)).values()
    }
   
   return render(request, 'produtos/home.html', produtos)

def scan_qrcode(request):
    if request.method == 'POST':
        qrcode = request.POST.get('qrcode')
        print(qrcode)
        return HttpResponse('OK')
    else:
        return render(request, 'base.html')




