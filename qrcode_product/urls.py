from django.urls import path
from app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('produtos', views.produtos, name='listagem_produtos'),
    path('produtos/filtro', views.filtroproduto, name='filtro_produtos'),
    path('produtos/<int:id>', views.excluirproduto, name='excluir_produto'),
    path('produtosCarrinho', views.produtosCarrinho, name='listagem_produtosCarrinho'),
    path('produtosCarrinho/filtro', views.filtroprodutoCarrinho, name='filtro_produtosCarrinho'),
    path('produtosCarrinho/<int:id>', views.excluirprodutoCarrinho, name='excluir_produtoCarrinho'),
   
]

