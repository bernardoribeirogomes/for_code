estoque = {"Celular" : [3, "Preto", 3500]}

chave = estoque.keys()
chave = list(chave)

linha1 = f"--- {chave[0]} {estoque["Celular"][1]} ---"
linha2 = f"Estoque: {estoque["Celular"][0]}"
linha3 = f"Valor total: {(estoque["Celular"][0])*(estoque["Celular"][2])}"

print(linha1)
print(linha2)
print(linha3)
