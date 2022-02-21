# Sobre
Este projeto foi construído para fins de aprendizado no framework [Scrapy](https://scrapy.org/), aplicado como ferramente de solução para um desafio envolvendo *crawler*.

## Descrição do Desafio
O objetivo do desafio é construir um programa que:
- Baixe todas as imagens do site xkcd.
- Salve as imagens localmente.
- O nome de cada arquivo deve ser o título **md5** do quadrinho (ex.: o nome do arquivo referente ao quadrinho https://xkcd.com/2563/ é ```dda012759b877051aba034de87eaef58.png```.
- Numa segunda vez que o programa for rodado, deve haver um verificador para que, caso o arquivo já exista, ele não seja salvo/sobrescrito localmente.
- O programa deve ter teste unitários.

## Tópicos estudados:
1. **[Virtualenv](https://virtualenv.pypa.io/en/latest/)**.
2. **[Scrapy](https://scrapy.org/)**.
3. **[Pytest e Unittest](https://docs.pytest.org/en/6.2.x/unittest.html)**.
4. **[Tox](https://tox.wiki/en/latest/#)**.
5. **[Shell Script](https://www.gnu.org/software/bash/manual/html_node/Shell-Scripts.html#Shell-Scripts)**.

## Metodologia Adotoda

A solução apresentada utiliza o framework **Scrapy** para criar um ***spider*** que realiza as seguintes ações:
- Acessa à *url* https://xkcd.com/archive/, onde são listados todos os *comics*. Recolhe o conteúdo de todas as *tags* **href** dentro do **div** que exibe os *links* das *comics*.
- Para cada **href** encontrado, é gerado uma *url* completa para navegar à página dos detalhes da *comic*. Dentro desta nova página, é extraída o conteúdo da *tag* **img** que armazena a fonte da imagem.
- Utilizando o conteído da *tag* **img**, caso exista, o ***spider*** envia este conteúdo ao [Pipeline de Itens](https://docs.scrapy.org/en/latest/topics/item-pipeline.html) responsável por realizar o *download* do conteúdo.
- Utilizando um [Pipeline de Itens](https://docs.scrapy.org/en/latest/topics/item-pipeline.html) customizado, o nome do arquivo foi alterado para representar o [md5](https://datatracker.ietf.org/doc/html/rfc1321.html) do conteúdo. Além disso, sempre que uma imagem é baixada, antes de persistir os dados, é verificado se um arquivo com mesmo nome, isto é, com mesmo conteúdo, já existe. Caso exista, a persistencia é ignorada.

### Exceções e Tratamentos
Alguns *link* de imagens obtidos através da *tag* **href** representam conteúdos dinâmicos, por exemplo as imagens https://xkcd.com/1416/ e https://xkcd.com/1608/. Para estes casos o *download* não é realizado. Isto ocorre para um total de 5 casos:
 - /1350/
 - /1416/
 - /1608/
 - /1663/
 - /2198/

## Requisitos
- Python 3.7
- Scrapy 2.5.1
- Pytest 2.5
- Tox 3.24.5

> Obs.: A solução foi construída sobre o **Pop!_OS 20.04 LTS**, sistema baseado no Ubuntu.

## Execução do Projeto:
1. Crie e inicie o ambiente virtual para o Python na versão 3.7:
    ```bash
    virtualenv -p python3.7 .venv && source .venv/bin/activate
    ```
2. Execute o script para instalação dos de requisitos para o Scrapy:
    ```bash
    bash scrapy_requirements.sh
    ```
3. Instale as dependências necessárias:
    ```bash
    pip install -r requirements/dev.txt
    ```
4. Execute na raiz do projeto o comando do Makefile
    ```bash
    make run-crawler
    ```

## Execução dos Testes:
1. Execute o tox utilizando:
    ```bash
    tox
    ```
2. Caso precise executar os testes somente sobre um arquivo especifico, utilize:
    ```bash
    tox -- -k <file-name>
    ```