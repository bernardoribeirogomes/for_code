# Sistema de Inventário de Laboratório 🧪

Este projeto em Python foi desenvolvido para gerenciar e automatizar a verificação do inventário de reagentes de um laboratório de Engenharia Química. 

## ⚙️ Funcionamento do Programa
O script processa os dados brutos exportados pelo laboratório (listas de reagentes, lotes e purezas) realizando as seguintes operações:
1. **Identificação**: Usa a estrutura `set()` para remover duplicações e contar quantos tipos únicos de reagentes o laboratório possui.
2. **Estruturação**: Une as informações desconexas das três listas iteráveis em uma única lista estruturada (lista de tuplas) utilizando a função `zip()`.
3. **Geração de Relatório**: Varre a lista unida através de um loop `for` utilizando a técnica de *unpacking* (desempacotamento) para exibir os dados de forma formatada e legível.
4. **Filtragem de Qualidade**: Emprega a técnica avançada de *List Comprehension* para filtrar e armazenar em uma nova lista apenas os códigos dos lotes que possuem um laudo de pureza maior ou igual a 98.0%, garantindo a segurança de experimentos sensíveis.

---

## 📚 Respostas das Perguntas Teóricas

**1. Levando em consideração a estrutura do nosso inventário, por que seria incorreto usar a função dict() para transformar o resultado do nosso zip() em um dicionário, utilizando o nome do reagente como "Chave" e o lote como "Valor"?**

Seria incorreto porque os dicionários em Python não permitem **chaves duplicadas**. No nosso inventário, o mesmo reagente (ex: 'Etanol') aparece várias vezes em frascos e lotes diferentes. Se usássemos o nome do reagente como chave, cada vez que o Python encontrasse um novo 'Etanol', ele sobrescreveria o lote anterior. No final, teríamos apenas um registro para cada reagente, perdendo os dados da maioria dos 30 frascos originais.

**2. O que a função zip() gera na memória do Python antes de usarmos a função list() para forçar a visualização dos dados?**

A função `zip()` gera um objeto iterador do tipo *generator* na memória, conhecido como "zip object". Esse objeto avalia e cria as tuplas sob demanda (de forma "preguiçosa" ou *lazy evaluation*), ou seja, ele não carrega todas as combinações na memória de uma vez só, o que economiza processamento. O uso da função `list()` força o Python a consumir esse iterador inteiro instantaneamente e despejar o resultado final na memória em formato de lista.

**3. Observando o seu código final, de que forma o List Comprehension substitui a necessidade de criar uma lista vazia e usar a estrutura de repetição for tradicional acompanhada do método .append()?**

A técnica de *List Comprehension* agrupa toda a lógica de criação de lista, o loop `for`, e a condição `if` em uma **única linha de código elegante e otimizada**. Em vez de declararmos uma variável como `lotes = []`, abrirmos um bloco de loop para varrer o inventário, abrirmos um bloco de `if` para testar a pureza e, só então, usarmos `lotes.append()`, nós dizemos ao Python: *"retorne o [lote] de cada item no loop [for... in...] caso a condição [if pureza >= 98] seja verdadeira"* — tudo diretamente dentro de colchetes `[]`.
