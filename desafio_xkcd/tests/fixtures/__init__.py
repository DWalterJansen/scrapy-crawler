import os
from PIL import Image
from scrapy.http import TextResponse, Request, Response


PATH_FIXTURES = ''


def response_from_file(arquivo, url=None, encoding='utf-8', meta={}, extensao='html', **kwargs):
    if not url:
        url = 'http://www.exemplo.com'

    request = Request(url=url, meta=meta, **kwargs)
    conteudo = obtem_fixture(arquivo, encoding, extensao)
    if type(conteudo) != str:
        return Response(url=url, request=request, body=conteudo)

    return TextResponse(url=url, request=request, body=conteudo, encoding=encoding)


def obtem_fixture(arquivo, encoding='utf-8', extensao='html'):
    if not arquivo[0] == '/':
        diretorio = os.path.dirname(os.path.realpath(__file__))
        caminho_arquivo = os.path.join(diretorio, PATH_FIXTURES, arquivo)
    else:
        caminho_arquivo = arquivo

    modo = 'r'
    with open(caminho_arquivo, modo, encoding=encoding) as f:
        return f.read()


# Add
def get_image_fixture(relative_path) -> Image:
    dir = os.path.dirname(os.path.realpath(__file__))
    global_path = os.path.join(dir, relative_path)
    return Image.open(global_path)
