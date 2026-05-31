# Dados do inventário físico (cada índice representa um frasco individual)
reagentes = ['Etanol', 'Acetona', 'Etanol', 'Ácido Sulfúrico', 'Benzeno', 'Acetona',
             'Etanol', 'Ácido Sulfúrico', 'Metanol', 'Tolueno', 'Etanol', 'Acetona', 
             'Ácido Acético', 'Etanol', 'Benzeno', 'Ácido Sulfúrico', 'Metanol', 
             'Ácido Acético', 'Etanol', 'Acetona', 'Tolueno', 'Ácido Sulfúrico', 
             'Benzeno', 'Etanol', 'Acetona', 'Metanol', 'Ácido Sulfúrico', 'Acetona', 
             'Ácido Acético', 'Etanol']

lotes = ['2023-ETA-01', '2023-ACE-01', '2023-ETA-01', '2023-SUL-01', '2023-BEN-01', 
         '2024-ACE-01', '2023-ETA-02', '2024-SUL-01', '2023-MET-01', '2024-TOL-01', 
         '2023-ETA-01', '2023-ACE-01', '2023-ACA-01', '2023-ETA-02', '2023-BEN-01', 
         '2023-SUL-01', '2023-MET-01', '2024-ACA-01', '2023-ETA-01', '2023-ACE-01', 
         '2024-TOL-01', '2024-SUL-01', '2023-BEN-01', '2023-ETA-01', '2024-ACE-01', 
         '2023-MET-01', '2023-SUL-01', '2024-ACE-01', '2024-ACA-01', '2023-ETA-02']

purezas = [99.5, 92.0, 99.5, 98.0, 99.9, 98.5, 96.0, 99.0, 99.0, 98.8, 99.5, 92.0, 99.2,
           96.0, 99.9, 98.0, 99.0, 95.0, 99.5, 92.0, 98.8, 99.0, 99.9, 99.5, 92.0, 99.0, 
           98.0, 98.5, 95.0, 96.0]

# 1. Identificação dos Tipos de Reagentes (Set)
# Utilizamos set() para remover duplicações e len() para contar os únicos.
reagentes_unicos = set(reagentes)
print(f"Quantidade total de reagentes diferentes: {len(reagentes_unicos)}\n")

# 2. Estruturação do Inventário (Zip)
# A função zip() junta as 3 listas e list() converte o resultado em uma lista de tuplas.
inventario = list(zip(reagentes, lotes, purezas))

# 3. Geração de Relatório (Unpacking)
# Utilizamos for com unpacking para extrair (reagente, lote, pureza) de cada tupla.
print("--- RELATÓRIO DE INVENTÁRIO ---")
for reagente, lote, pureza in inventario:
    print(f"Frasco do Lote: {lote} | Reagente: {reagente} | Pureza: {pureza}%")

# 4. Filtragem por Critério de Qualidade (List Comprehension)
# Criamos uma nova lista apenas com os lotes aprovados (pureza >= 98.0%) em uma linha.
lotes_aprovados = [lote for reagente, lote, pureza in inventario if pureza >= 98.0]

print("\n--- LOTES APROVADOS PARA EXPERIMENTOS SENSÍVEIS ---")
print(lotes_aprovados)
