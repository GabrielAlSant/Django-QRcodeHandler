from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos', views.produtos, name='listagem_produtos'),
    path('produtos/filtro', views.filtroproduto, name='filtro_produtos'),
     path('produtos/<int:id>', views.excluirproduto, name='excluir_produto'),
]

