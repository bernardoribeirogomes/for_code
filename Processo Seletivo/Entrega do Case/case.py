Case - Processo Seletivo Forcode
Autores: Bernardo Ribeiro, Gabriel Santiago, Juliana Mello, Isabel Lima Vallejo e Vitor Cóe

1. O Enigma do Número Secreto | 🔢
- Feito e comentado por: Vitor Cóe
Noção geral: O código deve primeiro gerar um número inteiro entre 1 e 50, ou seja, usar uma função que gere um número inteiro ou que gere um número e transforme ele em inteiro. Isso pode ser feito utilizando uma biblioteca e uma função que faça o número ser inteiro. Depois disso o código deve abrir uma caixa de texto utilizando o input, só que essa caixa deve ser verificada porque só pode aceitar números inteiros e deve verificar se é um número inteiro e não uma letra ou caractere especial, caso tenha tem que avisar que só aceita número inteiro, isso deve ser contado como tentativa. Se esse palpite for de um formato válido, esse deve ser comparado com o numero secreto, se maior deve ter a mensagem "maior que o número secreto", se for menor "Menor que número secreto" e se for o número secreto "Acertou!" e mostrar o número de tentativas. Com o adicional de se for 5 unidades próximados no número secreto deve adicionar "Quase lá"

#Objetivo 1: Gerar número inteiro entre 1 e 50 incluindo os dois limites.

import random #Nessa linha importou-se a biblioteca random, uma biblioteca capaz de gerar números pseudo-aleatórios. Essa biblioteca consegue gerar números dentro de intervalos, elementos dentro de sequências, permutações aleatórias e uma função para amostragem que pode ser útil para análise de dados.

numero_secreto = random.randint(1, 50) #Definiu-se a variável "numero_secreto" como o resultado da função random.randint(a,b) que conta com dois argumentos "a" e "b". Essa função gera um número inteiro no intervalo definido pelos dois argumentos e contendo os dois. Como a biblioteca foi importada antes a função funciona.

#Objetivo 2: Criar variável que será usada para contar tentativas

tentativas = 0 #Uma das metas do código é acompanhar o número de tentativas do usuário, pra isso deve ser criada uma variável de valor 0 a qual é somada 1 a cada vez que o jogador joga um palpite.

#Objetivo 3: Criar loop para rodar código até número_secreto ser descoberto

while True: #o while significa que enquanto for verdadeiro, o seguinte código abaixo (bloco) será executado, mas como true sempre é verdadeiro, cria-se um loop infinito que se ao final dele não encontrar um break, ele roda de novo

#Objetivo 4:Criar caixa de texto para usuário inserir palpite e toda vez que inserir um chute adicionar 1 ao número de tentativas

    palpite = input("Tente adivinhar um número inteiro entre 1 e 50: ") #estou definindo o meu palpite como um valor definido pelo usuário em uma caixa de texto, com o aviso para adivinhar um número inteiro entre 1 e 50

    tentativas += 1 #toda vez que o código rodar eu aumento em um o número de tentativas, independente se a entrada é válida ou não, assim o número final de tentativas independe da entrada ser ou não válida.

#Objetivo 5: Testar se o palpite é um número inteiro, sem letras e caracteres especiais. Se testar e não for o código não deve quebrar, deve abrir uma nova caixa de texto e avisar ao usuário

    try: #quero saber se o seguinte código vai dar erro, controle do fluxo baseado no tratamento do erro
        palpite = int(palpite) #testo se o palpite é um número inteiro, se não for vai dar erro sem quebrar o código, pois pula pro except. Se não der erro, o bloco do except não é rodado.
    except ValueError: #Caso o palpite não seja um inteiro,
        print("Entrada inválida! Digite um número inteiro.") #só printa essa mensagem se o try tiver retornado o ValueError e entrar no bloco do except
        continue #Essa linha serve pro código voltar imediatamente pro início do loop do while, sem rodar o resto das linhas

#Objetivo 6: Comparar palpite com número secreto, se palpite for igual, o código para, se não for tem que continuar rodando e avisar se o palpite está acima ou abaixo do numero_secreto

    if palpite == numero_secreto: #comparo valor do palpite com o número secreto, == é diferente de =, um é comparação e outro é atribuir valor pra variável, nessa caso estamos comparando
        print(f"Acertou! Número de tentativas: {tentativas}") #se a comparação for verdadeira vai printar a mensagem, esse f faz com que a string seja um f-string e o que está dentro das chaves é lido como código, se não tivesse isso apareceria literalmente ""Acertou! Número de tentativas: {tentativas}""
        break #para a repetição do código, o código só para quando o usuário acerta o código porque essa linha só é lida caso o usuário tenha dado um palpite igual ao numero_secreto.
#caso o if acima não seja verdadeiro, ele é ignorado, então o código não para e executa pra dar as dicas pedidas.
    if palpite > numero_secreto: #se palpite for maior que número secreto avisa que foi maior.
        print("Maior do que o número secreto.")
    else: #Se palpite ser maior que número secreto for false, executa o else no lugar do if e fala que é menor que o número secreto, poderia ser dividido em dois "if"s mas ficaria repetitivo.
        print("Menor do que o número secreto.")

#Objetivo 7: Checar se distância entre o numero_secreto e palpite é menor que 5, se for avisar.

    if abs(palpite - numero_secreto) <= 5: #o abs tira o módulo do argumento, se o módulo, ou seja distância na reta real, for menor ou igual a 5 o código avisa que está quase lá
        print("Quase lá!")
        #como não teve break no final do código, volta pro início do while

2. O Sistema de Cashback | Juliana Mello
# Comentários realizados por Juliana Mello

'''

A questão pedia:

Um sistema de compras em que cada cliente tem uma lista de compras realizadas.
O sistema dá um bônus de 10% de cashback apenas para os clientes que gastaram mais de R$500,00 no total
(somando todas as suas compras).

Entrada: um dicionário onde a chave é o nome do cliente e o valor é uma lista com os preços das compras feitas por ele.
Desafio: Criar um novo dicionário que contenha apenas os clientes que têm direito ao cashback.
A chave deve ser o nome do cliente e o valor deve ser o valor total do cashback que ele vai receber.

'''


def calcular_cashback(compras_clientes): # aqui, é criada uma função (calcular_cashback) que vai receber o parâmetro compras_clientes (o dicionário)
    cashback = {} # um dicionário "cashback" vazio que vai receber o resultado


# o que a função fará:
    # primeiro, um loop que garante que ela irá percorrer todas as chaves e seus respectivos elementos dentro do dicionário de entrada
    for cliente in compras_clientes: # ela vai executar esses comandos enquanto a chave existir dentro de "compras_clientes"
        total = sum(compras_clientes[cliente]) # a variável "total" é a soma de todos os valores dentro de cada chave

        if total > 500: # condicional, só vai fazer as linhas de baixo se obedecer a soma dos valores ser maior do que 500
            cashback[cliente] = total * 0.1 # coloca no dicionário "cashback" a chave (nome do cliente com total > 500) o valor do seu cashback, que é 10% do total

    return cashback # retorna esse dicionário de cashback


compras_clientes = { # dicionário de entrada, com os nomes do clientes e quanto cada um gastou em cada compra
    "Ana": [100, 200, 50],
    "Bruno": [600, 100],
    "Carla": [50, 50, 50, 50],
    "Diego": [1000]
}

resultado = calcular_cashback(compras_clientes) # "resultado" guarda o dicionario "cashback", que é gerado após implementar a função "calcular_cashback" no dicionário de entrada ("compras_clientes")
print(resultado) # printa na tela esse dicionário de cashback, o resultado

3. O Labirinto de Dados (Compressão de Sequências) | Isabel Lima
# Para dada sequência numérica, o objetivo é identificar a maior sequência de números iguais que aparecem consecutivamente (platô)
# A intenção não é contar quantas vezes um número aparece no total, mas contar quantas vezes ele aparece em sequência

# Definição das variáveis
dados = [1, 2, 2, 3, 3, 3, 4, 4, 1, 1, 1, 1, 5, 5, 5]

maior_valor = dados[0] # É importante pegar o primeiro elemento da lista para evitar alguma lista vazia
maior_repeticao = 1    # Foi assumido que inicialmente o primeiro número já é o maior (por enquanto) e ele aparece 1 vez

valor_atual = dados[0]
repeticao_atual = 1    # Aqui é armazenado a informação de qual número está sendo analisado e quantas vezes ele aparece consecutivamente

# Em síntese: defini-se que o valor atual é o primeiro número da lista e que ele aparece uma vez. Ao mesmo tempo, conside-se que esse também é o maior platô, com repetição = 1.

for i in range(1, len(dados)):   # Iniciar a lista a partir do segundo elemento
    if dados[i] == dados[i - 1]: # Precisa retirar 1 pois ao começar em zero daria erro pelo que foi definido na linha anterior
        repeticao_atual += 1     # Se o número atual é igual ao anterior, tem mesmo plato e a contagem aumenta. Então, isso verifica a continuidade da sequência
    else:                        # Quebra do looping, quebra da sequência
        repeticao_atual = 1      # Atualização do valor atual e reinicia a contagem para 1, caso o elemento for diferente do anterior
        valor_atual = dados[i]

    if repeticao_atual > maior_repeticao:    # Indicar que para sempre encontrar um plato maior, deve guardar qual número gerou esse platô
        maior_repeticao = repeticao_atual   # Foi considerado > e não >= para, em caso de empate, retornar o que apareceu primeiro e só atualizar se for realmente maior, salvando o primeiro. (sempre guardar o que for maior que o anterior)
        maior_valor = dados[i]

# Em síntese: Se o número atual for igual ao anterior, continua-se a sequência e aumenta a contagem; se for diferente, começa-se uma nova sequência com contagem = 1.
# Cada passo é comparado com o maior platô já encontrado e será atualizado se for maior. Ao final, o número com maior sequência e quantidade é retornado.

print(f"Valor: {maior_valor}, Repetições: {maior_repeticao}") # Exibe o resultado. O 'f' é usado quando o resultado é um número, como nesse caso

4. Filtro de Qualidade de Sensores (Deep Data) | Comentários realizados pelos alunos Bernardo Ribeiro e Gabriel Santiago

#Comentários realizados pelos alunos Bernardo Ribeiro e Gabriel Santiago

import numpy as np  # Importa o NumPy, porque o enunciado pede uma matriz NumPy, não uma lista comum.

# Cria a matriz de dados.
# Cada linha representa um sensor.
# Cada coluna representa uma leitura daquele sensor ao longo do dia.
dados = np.array([
    [25, 30, 35],   # Sensor 0
    [10, 85, 20],   # Sensor 1
    [45, 55, 60],   # Sensor 2
    [-5, 20, 25]    # Sensor 3
])

instaveis = []  # Lista onde vamos guardar apenas os índices dos sensores instáveis.

# Usamos for i in range(len(dados)) porque o exercício quer os índices dos sensores.
# Como cada linha da matriz é um sensor, i vai assumir os valores 0, 1, 2 e 3. | Bernardo
for i in range(len(dados)):

    # Guardamos dados[i] em uma variável chamada leituras para o código ficar mais legível.
    # Assim, evitamos repetir dados[i] várias vezes ao longo do programa.
    leituras = dados[i]

    # Criamos uma lista vazia de motivos.
    # Isso é importante porque um mesmo sensor pode ser instável por mais de um motivo.
    motivos = []

    # np.any(...) é usado quando queremos saber se existe pelo menos um valor
    # que viola a regra.
    # Aqui, verificamos se existe alguma leitura acima de 80°C.
    if np.any(leituras > 80):
        # Além de verificar se existe uma leitura acima de 80,
        # também salvamos exatamente quais valores causaram esse problema.
        valores_acima_80 = [int(valor) for valor in leituras[leituras > 80]]
        motivos.append(f"Leitura acima de 80°C: {valores_acima_80}")

    # Novamente usamos np.any(...), agora para verificar
    # se existe alguma leitura abaixo de 0°C.
    if np.any(leituras < 0):
        # Convertemos cada valor para int comum do Python
        # para a exibição não aparecer como np.int64(...)
        valores_abaixo_0 = [int(valor) for valor in leituras[leituras < 0]]
        motivos.append(f"Leitura abaixo de 0°C: {valores_abaixo_0}")

    # np.mean(...) calcula a média das leituras.
    # Usamos essa função porque um dos critérios de instabilidade
    # é ter média maior que 50°C.
    media = np.mean(leituras)

    if media > 50:
        # Guardamos a média formatada com duas casas decimais
        # para a saída ficar mais clara e mais bonita.
        motivos.append(f"Média instável: {media:.2f}°C")

    # Se a lista de motivos não estiver vazia,
    # significa que o sensor foi considerado instável por pelo menos um critério.
    if len(motivos) > 0:
        # Guardamos o índice do sensor na lista de instáveis,
        # porque o enunciado pede os índices.
        instaveis.append(i)

        # Exibimos o número do sensor.
        print(f"Sensor {i} está instável por:")

        # Percorremos todos os motivos encontrados para esse sensor.
        # Isso é importante porque um sensor pode falhar por mais de um motivo.
        for motivo in motivos:
            print(f"  - {motivo}")

# Ao final, mostramos a lista com os índices de todos os sensores instáveis.
print(f"Índices dos sensores instáveis: {instaveis}")
