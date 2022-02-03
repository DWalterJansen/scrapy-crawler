# Sobre
Este projeto foi construído para fins de aprendizado no framework [Scrapy](https://scrapy.org/), aplicado como ferramente de solução para um desafio envolvendo *crawlers*.

## Descrição do Desafio

## Tópicos estudados:
1. **[Virtualenv](https://virtualenv.pypa.io/en/latest/)**.
2. **[Scrapy](https://scrapy.org/)**.
3. **[Pytest e Unittest](https://docs.pytest.org/en/6.2.x/unittest.html)**.
4. **[Tox](https://tox.wiki/en/latest/#)**.
5. **[Shell Script](https://www.gnu.org/software/bash/manual/html_node/Shell-Scripts.html#Shell-Scripts)**.

## Metodologia Adotoda

## Arquitetura da Solução:

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