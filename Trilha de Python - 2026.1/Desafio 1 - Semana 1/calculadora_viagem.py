# Planejador de Viagens

orcamento = float(input("Olá, Mariana! Planejando a próxima aventura? Deixa eu te ajudar com isso, digite o valor disponível, em reais: "))
destino = input("Hm, temos um bom orçamento para começar... e qual o destino dos sonhos que você cogitou? Digite aqui: ")
custo_passagem = float(input("Uauu, que sonho! Qual o valor da passagem para esse destino iradíssimo? Me conte aqui: "))
hospedagem_euro = float(input("Já consigo sentir o frio europeu daqui, agora me conte sobre o custo diário da hospedagem, em euros: "))
duracao = int(input("Para finalizar, Mariana! Quantos dias de aventura você está planejando? Fale por aqui: "))

# Validação: nenhum valor numérico pode ser negativo
if orcamento < 0 or custo_passagem < 0 or hospedagem_euro < 0 or duracao < 0:
    print("Erro: nenhum valor numérico pode ser negativo.")
    exit()

# Conversão de moeda
cotacao_euro = 6.10
hospedagem_brl = hospedagem_euro * cotacao_euro

# Cálculo do valor total da hospedagem
valor_total_hospedagem = hospedagem_brl * duracao

# Cálculo do custo total da viagem
custo_total = custo_passagem + valor_total_hospedagem

# Validação do orçamento
if custo_total <= orcamento:
    status_orcamento = "Orçamento possível"
else:
    status_orcamento = "Orçamento não possível"

# Status final da viagem
viavel = (custo_total <= orcamento) and (duracao > 0)

if viavel:
    status_final = "Viável"
else:
    status_final = "Inviável"

# Cálculo de sobra ou falta
diferenca = orcamento - custo_total

print("\n===== RESUMO DA VIAGEM =====")
print(f"Destino: {destino}")
print(f"Valor total da hospedagem em reais: R$ {valor_total_hospedagem:.2f}")
print(f"Custo total da viagem em reais: R$ {custo_total:.2f}")
print(f"Status do orçamento: {status_orcamento}")
print(f"Status final da viagem: {status_final}")
print(f"Viável: {viavel}")

if diferenca >= 0:
    print(f"Sobram R$ {diferenca:.2f} no orçamento.")
else:
    print(f"Faltam R$ {abs(diferenca):.2f} para realizar a viagem.")
