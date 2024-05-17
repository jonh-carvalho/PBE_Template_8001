# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.produto_list, name='produto_list'),
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('clientes/novo/', views.cliente_create, name='cliente_create'),
    path('clientes/editar/<int:pk>/', views.cliente_edit, name='cliente_edit'),
    path('clientes/excluir/<int:pk>/', views.cliente_delete, name='cliente_delete'),

    path('produtos/', views.produto_list, name='produto_list'),
    path('produtos/<int:pk>/', views.produto_detail, name='produto_detail'),
    path('produtos/novo/', views.produto_create, name='produto_create'),
    path('produtos/editar/<int:pk>/', views.produto_edit, name='produto_edit'),
    path('produtos/excluir/<int:pk>/', views.produto_delete, name='produto_delete'),
]
