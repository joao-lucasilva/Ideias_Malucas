from django.urls import path, include
from website.views import index, sobre, cadastro, cadastrar_ideia, remover_ideia

urlpatterns = [
    path('', index),
    path('sobre', sobre),
    path('cadastro', cadastro),
    path('ideias', cadastrar_ideia),
    path('remover_ideia/<int:id>', remover_ideia)
]
