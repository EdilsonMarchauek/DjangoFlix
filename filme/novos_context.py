from .models import Filme

# incluir no settings templates


def lista_filmes_recentes(request):
    # -data_criação -> menos na frente ordem decrescente
    # "lista_filmes_recentes -> chave do dicionario que vai para o html
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]
    if lista_filmes:
        filme_destaque = lista_filmes[0]
    else:
        filme_destaque = None
    return {"lista_filmes_recentes": lista_filmes, "filme_destaque": filme_destaque}


def lista_filmes_emalta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:10]
    return {"lista_filmes_emalta": lista_filmes}


