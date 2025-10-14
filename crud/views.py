# Em crud/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa

# ------------------------------------------------------------------
# VIEWS QUE ESTAVAM FALTANDO
# ------------------------------------------------------------------

# ADICIONADO: Função para criar uma nova pessoa no banco de dados.
def salvar(request):
    if request.method == 'POST':
        nome_recebido = request.POST.get('nome')
        idade_recebida = request.POST.get('idade')
        
        if nome_recebido and idade_recebida: # Garante que não salve dados vazios
            Pessoa.objects.create(nome=nome_recebido, idade=idade_recebida)
            return redirect('home')
            
    # Se não for POST ou se os dados estiverem vazios, apenas volta para a home
    return redirect('home')


# ADICIONADO: Função para apagar uma pessoa pelo ID.
def apagar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    pessoa.delete()
    return redirect('home')

# ------------------------------------------------------------------
# SUAS VIEWS CORRIGIDAS E MANTIDAS
# ------------------------------------------------------------------

# MANTIDO: Sua função 'editar' já estava perfeita.
def editar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    return render(request, 'editar.html', {'pessoa': pessoa})


# CORRIGIDO E RENOMEADO: Sua função 'update' com a correção no redirect.
# Renomeei para 'atualizar' para manter a consistência com o urls.py
def atualizar(request, id):
    if request.method == 'POST':
        pessoa = get_object_or_404(Pessoa, id=id)
        pessoa.nome = request.POST.get('nome')
        pessoa.idade = request.POST.get('idade')
        pessoa.save()
        # CORREÇÃO: O redirect deve usar o NOME da URL como string.
        return redirect('home') # <--- CORRIGIDO de redirect(home) para redirect('home')
        
    # Se alguém tentar acessar a URL de atualizar via GET, redireciona para a home.
    return redirect('home')


# MANTIDO: Sua função 'home' já estava perfeita.
def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas': pessoas})