# for_code

## Liga Acadêmica de Computação da Escola de Química da UFRJ

Atualmente estou realizando a **Trilha de Python 2026.2**, uma capacitação interna de nivelamento na linguagem de programação oficial da Liga Acadêmica.

---

# Semana 1 — Trilha de Python 2026.2

## Desafio Semanal: Sistema de Auxílio ao Orçamento de Viagens

Este programa foi desenvolvido em Python para auxiliar no planejamento financeiro de uma viagem.

A proposta é simples: o usuário informa o orçamento disponível, o destino desejado, o valor da passagem, o custo diário da hospedagem em euros e a quantidade de dias da viagem. A partir desses dados, o programa calcula o custo total da viagem e informa se o orçamento é suficiente ou não.

---

## Como o programa funciona

O programa solicita as seguintes informações:

```bash
Wish> Valor disponível para a viagem
Wish> Destino desejado
Wish> Valor da passagem
Wish> Custo diário da hospedagem em euros
Wish> Quantidade de dias da viagem
```

Depois disso, o sistema:

1. Converte o valor da hospedagem de euro para real;
2. Calcula o custo total da hospedagem;
3. Soma o valor da passagem com o valor total da hospedagem;
4. Compara o custo total com o orçamento disponível;
5. Informa se a viagem é viável ou inviável;
6. Mostra quanto sobra ou quanto falta no orçamento.

---

## Exemplo de uso

```bash
prompt> python3 calculadora_viagem_py.py

Olá, Mariana! Planejando a próxima aventura? Deixa eu te ajudar com isso, digite o valor disponível, em reais: 8000
Hm, temos um bom orçamento para começar... e qual o destino dos sonhos que você cogitou? Digite aqui: Paris
Uauu, que sonho! Qual o valor da passagem para esse destino iradíssimo? Me conte aqui: 3500
Já consigo sentir o frio europeu daqui, agora me conte sobre o custo diário da hospedagem, em euros: 70
Para finalizar, Mariana! Quantos dias de aventura você está planejando? Fale por aqui: 5

===== RESUMO DA VIAGEM =====
Destino: Paris
Valor total da hospedagem em reais: R$ 2135.00
Custo total da viagem em reais: R$ 5635.00
Status do orçamento: Orçamento possível
Status final da viagem: Viável
Viável: True
Sobram R$ 2365.00 no orçamento.
```

---

## Código comentado linha por linha

```python
# -*- coding: utf-8 -*-
# Define a codificação do arquivo como UTF-8, permitindo o uso de acentos e caracteres especiais.

# Planejador de Viagens
# Título informal do programa.

orcamento = float(input("Olá, Mariana! Planejando a próxima aventura? Deixa eu te ajudar com isso, digite o valor disponível, em reais: "))
# Recebe o orçamento disponível informado pelo usuário.
# Como input() retorna texto, usamos float() para converter o valor para número decimal.

destino = input("Hm, temos um bom orçamento para começar... e qual o destino dos sonhos que você cogitou? Digite aqui: ")
# Recebe o destino da viagem.
# Aqui não é necessário converter, pois o destino é um texto.

custo_passagem = float(input("Uauu, que sonho! Qual o valor da passagem para esse destino iradíssimo? Me conte aqui: "))
# Recebe o valor da passagem.
# Usamos float() porque valores em dinheiro podem ter casas decimais.

hospedagem_euro = float(input("Já consigo sentir o frio europeu daqui, agora me conte sobre o custo diário da hospedagem, em euros: "))
# Recebe o custo diário da hospedagem em euros.
# Também usamos float(), pois é um valor monetário.

duracao = int(input("Para finalizar, Mariana! Quantos dias de aventura você está planejando? Fale por aqui: "))
# Recebe a duração da viagem em dias.
# Usamos int(), pois a quantidade de dias deve ser um número inteiro.

if orcamento < 0 or custo_passagem < 0 or hospedagem_euro < 0 or duracao < 0:
    print("Erro: nenhum valor numérico pode ser negativo.")
    exit()
# Verifica se algum valor numérico digitado é negativo.
# Caso exista valor negativo, o programa exibe uma mensagem de erro e encerra a execução.

cotacao_euro = 6.10
# Define a cotação fixa do euro utilizada no programa.

hospedagem_brl = hospedagem_euro * cotacao_euro
# Converte o valor diário da hospedagem de euro para real.

valor_total_hospedagem = hospedagem_brl * duracao
# Calcula o valor total da hospedagem multiplicando o custo diário pela quantidade de dias.

custo_total = custo_passagem + valor_total_hospedagem
# Calcula o custo total da viagem somando passagem e hospedagem.

if custo_total <= orcamento:
    status_orcamento = "Orçamento possível"
else:
    status_orcamento = "Orçamento não possível"
# Compara o custo total da viagem com o orçamento disponível.
# Se o custo for menor ou igual ao orçamento, a viagem cabe no orçamento.

viavel = (custo_total <= orcamento) and (duracao > 0)
# Cria uma variável booleana para indicar se a viagem é viável.
# A viagem só é viável se o orçamento for suficiente e a duração for maior que zero.

if viavel:
    status_final = "Viável"
else:
    status_final = "Inviável"
# Transforma o resultado booleano em uma mensagem textual para o usuário.

diferenca = orcamento - custo_total
# Calcula a diferença entre o orçamento disponível e o custo total da viagem.
# Se o resultado for positivo, sobra dinheiro.
# Se for negativo, falta dinheiro.

print("\n===== RESUMO DA VIAGEM =====")
# Exibe o título do resumo final.
# O \n pula uma linha antes do texto.

print(f"Destino: {destino}")
# Exibe o destino informado pelo usuário.

print(f"Valor total da hospedagem em reais: R$ {valor_total_hospedagem:.2f}")
# Exibe o valor total da hospedagem formatado com duas casas decimais.

print(f"Custo total da viagem em reais: R$ {custo_total:.2f}")
# Exibe o custo total da viagem formatado com duas casas decimais.

print(f"Status do orçamento: {status_orcamento}")
# Mostra se o orçamento é suficiente ou não.

print(f"Status final da viagem: {status_final}")
# Mostra se a viagem é viável ou inviável.

print(f"Viável: {viavel}")
# Exibe o valor booleano da análise: True para viável e False para inviável.

if diferenca >= 0:
    print(f"Sobram R$ {diferenca:.2f} no orçamento.")
else:
    print(f"Faltam R$ {abs(diferenca):.2f} para realizar a viagem.")
# Se a diferença for positiva ou zero, o programa informa quanto sobra.
# Se a diferença for negativa, usa abs() para mostrar o valor que falta sem sinal negativo.
```

---

## Conceitos de Python utilizados

- `input()` para receber dados digitados pelo usuário;
- `float()` para converter textos em números decimais;
- `int()` para converter textos em números inteiros;
- variáveis para armazenar informações;
- operadores matemáticos para realizar cálculos;
- operadores de comparação, como `<`, `<=` e `>=`;
- operadores lógicos, como `or` e `and`;
- estruturas condicionais com `if` e `else`;
- f-strings para formatar mensagens de saída;
- validação de dados para impedir valores negativos;
- uso de valores booleanos, como `True` e `False`.

---

## Aplicações práticas

Esse programa pode servir como base para sistemas simples de:

- planejamento de viagens;
- controle de gastos pessoais;
- simulação de orçamento;
- comparação entre destinos;
- análise de viabilidade financeira.

Mesmo sendo um projeto introdutório, ele trabalha uma lógica essencial da programação:

```text
entrada de dados → processamento → saída de informações úteis
```

---

# Perguntas teóricas

## 1. Qual é a diferença entre `git add .` e `git commit -m "mensagem"`?

O comando:

```bash
git add .
```

envia as alterações feitas nos arquivos para a área de preparação do Git, chamada de *staging area*.

Isso significa que o Git passa a considerar aquelas alterações como parte do próximo registro do projeto.

Já o comando:

```bash
git commit -m "mensagem"
```

salva definitivamente essas alterações no histórico do repositório, criando uma nova versão do projeto acompanhada de uma mensagem explicando o que foi feito.

Em resumo:

```bash
prompt> git add .
```

prepara as alterações.

```bash
prompt> git commit -m "mensagem"
```

registra as alterações no histórico do projeto.

---

## 2. Por que precisamos converter o resultado de `input()` usando `int()` ou `float()`?

A função `input()` sempre recebe os dados digitados pelo usuário como texto, ou seja, como uma `string`.

Mesmo que o usuário digite um número, o Python inicialmente entende esse valor como texto.

Por exemplo:

```python
valor = input("Digite um número: ")
```

Se o usuário digitar `100`, o Python armazenará `"100"` como texto, não como número.

Por isso, quando queremos fazer contas, precisamos converter esse valor:

```python
orcamento = float(input("Digite o orçamento: "))
dias = int(input("Digite a quantidade de dias: "))
```

Usamos:

- `int()` para números inteiros, como quantidade de dias;
- `float()` para números decimais, como valores em dinheiro.

---

## 3. O que acontece se tentarmos somar uma string com um número?

O Python gera um erro do tipo `TypeError`, porque ele não soma automaticamente texto com número.

Exemplo incorreto:

```python
resultado = "100" + 50
```

Nesse caso, `"100"` é uma string e `50` é um número inteiro. Como são tipos diferentes, o Python não sabe se deve fazer uma soma matemática ou uma concatenação de texto.

A forma correta é converter a string antes da operação:

```python
resultado = float("100") + 50
print(resultado)
```

Saída:

```python
150.0
```

Esse cuidado é muito importante em programas que usam `input()`, porque tudo que vem do usuário chega primeiro como texto.

---

## Conclusão

O desafio da Semana 1 foi importante para praticar conceitos fundamentais de Python, como entrada de dados, conversão de tipos, operações matemáticas, condicionais, validação e formatação de saída.

Além disso, o programa mostra como a lógica de programação pode ser aplicada a situações reais, como verificar se uma viagem cabe ou não dentro de um orçamento.
