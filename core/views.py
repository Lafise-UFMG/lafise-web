from django.shortcuts import render

def home(request):
    """View para a página inicial (landing page)"""
    context = {
        'page_title': 'Laboratório de Fisiologia do Exercício - UFMG',
        'page_description': 'Ferramenta de documentação e gerenciamento de materiais e métodos do laboratório de fisiologia do exercício UFMG'
    }
    return render(request, 'core/home.html', context)

def referencias(request):
    """View para a página de Principais Referências Bibliográficas"""
    context = {
        'page_title': 'Principais Referências Bibliográficas'
    }
    return render(request, 'core/referencias.html', context)

def agenda(request):
    """View para a página de Agenda"""
    context = {
        'page_title': 'Agenda do Laboratório'
    }
    return render(request, 'core/agenda.html', context)

def metodos_softwares(request):
    """View para a página de Métodos e Softwares"""
    context = {
        'page_title': 'Métodos e Softwares'
    }
    return render(request, 'core/metodos_softwares.html', context)

def metodos(request):
    """View para a página de Métodos"""
    context = {
        'page_title': 'Métodos de Pesquisa'
    }
    return render(request, 'core/metodos.html', context)

def artigos(request):
    """View para a página de Artigos"""
    context = {
        'page_title': 'Artigos Publicados'
    }
    return render(request, 'core/artigos.html', context)

def equipamentos(request):
    """View para a página de Equipamentos"""
    context = {
        'page_title': 'Equipamentos do Laboratório'
    }
    return render(request, 'core/equipamentos.html', context)

def integrantes(request):
    """View para a página de Integrantes"""
    context = {
        'page_title': 'Integrantes do Laboratório'
    }
    return render(request, 'core/integrantes.html', context)

def grupo_cafezinho(request):
    """View para a página do Grupo Do Cafezinho"""
    context = {
        'page_title': 'Grupo Do Cafezinho'
    }
    return render(request, 'core/grupo_cafezinho.html', context)

def historia(request):
    """View para a página de História"""
    context = {
        'page_title': 'História do Laboratório'
    }
    return render(request, 'core/historia.html', context)

def test_bootstrap(request):
    """View de teste para verificar se o Bootstrap está funcionando"""
    return render(request, 'test_bootstrap.html')
