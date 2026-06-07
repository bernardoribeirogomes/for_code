# Desafio 4 — Automação de Versionamento de Diretórios Vazios

Este projeto foi desenvolvido para automatizar o versionamento de diretórios vazios em um repositório Git.

## Contexto

O Git não versiona diretórios vazios. Para contornar isso, é comum utilizar um arquivo chamado `.gitkeep` dentro desses diretórios. Dessa forma, mesmo que a pasta não tenha nenhum arquivo real, ela passa a ser reconhecida e versionada pelo Git.

Por convenção, o arquivo `.gitkeep` deve existir apenas em diretórios vazios. Caso um diretório deixe de ser vazio, o `.gitkeep` deve ser removido.

## Objetivo do programa

O programa percorre os diretórios de um repositório local e aplica automaticamente as seguintes regras:

1. Se o diretório estiver vazio, o programa cria um arquivo `.gitkeep`.
2. Se o diretório não estiver vazio e possuir um `.gitkeep`, o programa remove esse arquivo.
3. O diretório `logs` não é processado pelo algoritmo.
4. A cada execução, o programa registra um histórico em `logs/log.json`.

## Como o programa funciona

O arquivo principal é o `main.py`.

Ao ser executado, ele realiza as seguintes etapas:

1. Define o caminho do repositório que será processado.
2. Cria o diretório `logs`, caso ele ainda não exista.
3. Percorre todos os diretórios do projeto, ignorando `logs` e `.git`.
4. Verifica se cada diretório está vazio ou não.
5. Cria `.gitkeep` em diretórios vazios.
6. Remove `.gitkeep` de diretórios que possuem outros arquivos ou subdiretórios.
7. Atualiza o arquivo `logs/log.json` com:

   * data e hora da execução;
   * arquivos `.gitkeep` criados;
   * arquivos `.gitkeep` removidos.

## Como usar

Clone ou baixe o repositório e execute o arquivo `main.py` na raiz do projeto:

```bash
python main.py
```

Também é possível informar o caminho de outro diretório manualmente:

```bash
python main.py caminho/do/repositorio
```

Exemplo:

```bash
python main.py coisas-da-universidade
```

## Exemplo de estrutura antes da execução

```text
coisas-da-universidade/
├── Estagios/
├── Monitorias/
├── Iniciacao-Cientifica/
├── Materias/
│   └── calculo.pdf
└── main.py
```

## Exemplo de estrutura depois da execução

```text
coisas-da-universidade/
├── Estagios/
│   └── .gitkeep
├── Monitorias/
│   └── .gitkeep
├── Iniciacao-Cientifica/
│   └── .gitkeep
├── Materias/
│   └── calculo.pdf
├── logs/
│   └── log.json
└── main.py
```

## Exemplo de log gerado

```json
{
    "execucoes": [
        {
            "data_hora": "2026-06-07T19:50:00",
            "arquivos_gitkeep_criados": [
                "Estagios/.gitkeep",
                "Monitorias/.gitkeep",
                "Iniciacao-Cientifica/.gitkeep"
            ],
            "arquivos_gitkeep_removidos": []
        }
    ]
}
```

## Perguntas teóricas

### Diferença entre `json.dump()` e `json.dumps()`

A função `json.dump()` transforma um objeto Python em JSON e grava diretamente esse conteúdo em um arquivo.

Exemplo:

```python
import json

dados = {"nome": "Pedro", "curso": "Python"}

with open("dados.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
```

Já a função `json.dumps()` transforma um objeto Python em uma string no formato JSON, sem salvar diretamente em um arquivo.

Exemplo:

```python
import json

dados = {"nome": "Pedro", "curso": "Python"}

texto_json = json.dumps(dados, indent=4, ensure_ascii=False)

print(texto_json)
```

Portanto:

* `json.dump()` grava JSON em um arquivo.
* `json.dumps()` retorna uma string JSON.

### Diferença entre `json.load()` e `json.loads()`

A função `json.load()` lê um arquivo JSON e transforma seu conteúdo em um objeto Python.

Exemplo:

```python
import json

with open("dados.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

print(dados)
```

Já a função `json.loads()` lê uma string em formato JSON e transforma essa string em um objeto Python.

Exemplo:

```python
import json

texto_json = '{"nome": "Pedro", "curso": "Python"}'

dados = json.loads(texto_json)

print(dados)
```

Portanto:

* `json.load()` lê JSON a partir de um arquivo.
* `json.loads()` lê JSON a partir de uma string.

## Conclusão

O programa resolve o problema de versionamento de diretórios vazios no Git de forma automática. Ele mantém `.gitkeep` apenas onde é necessário, remove arquivos desnecessários e registra todas as alterações em um arquivo de log, garantindo organização e rastreabilidade.
