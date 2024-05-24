from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Pessoa

# Create your views here.

def home(request):
    # Consulta diretamente as pessoas no banco de dados
    pessoas = Pessoa.objects.all()
    

    # Agora você pode usar a variável 'pessoas' na renderização da página home
    return render(request, 'index.html', {'pessoas': pessoas})

def add_pessoa(request):
    if request.method == 'POST':
        # Processar os dados do formulário aqui
        avatar = request.POST.get('avatar')
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        whatsapp = request.POST.get('whatsapp')
        data_cadastro = request.POST.get('dataCadastro')

        # Crie uma instância do modelo Pessoa
        pessoa = Pessoa(
            avatar=avatar,
            nome=nome,
            descricao=descricao,
            whatsapp=whatsapp,
            data_cadastro=data_cadastro
        )

        # Salve a pessoa no banco de dados
        pessoa.save()

        # Redirecione para a página desejada após o cadastro
        return render(request,'cadastro_sucess.html')

    return render(request, 'index.html')

def delete_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    pessoa_nome = pessoa.nome  # Adicione esta linha para obter o nome da pessoa
    if request.method == 'POST':
        pessoa.delete()
        return redirect('home')
    return render(request, 'delete_pessoa.html', {'pessoa': pessoa, 'pessoa_nome': pessoa_nome})


def editar_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)

    if request.method == 'POST':
        pessoa.nome = request.POST.get('nome')
        pessoa.descricao = request.POST.get('descricao')
        pessoa.whatsapp = request.POST.get('whatsapp')
        pessoa.dataCadastro = request.POST.get('dataCadastro')
        pessoa.save()
        return redirect('home')

    return render(request, 'editar_pessoa.html', {'pessoa': pessoa})