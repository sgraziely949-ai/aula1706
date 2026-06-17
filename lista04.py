# Descobrindo o tamanho da lista
nomes = ["Wilson", "Bianca", "Ronaldo", "Silmara", "Juliano"]

print(len(nomes))

# saber se existe um elemento na lista
if "Wilson" in nomes:
    print("está na lista")
else:
    print("não está na lista")
# A posição não está na lista
indice = nomes.index("Bianca")
print(f"A Bianca está no indice {indice}")

# Percorrer a lista
for nome in nomes:
    print(nome)

# Percorrer a lista com índice e valor
for name, nome in enumerate(nomes):
    print(name, nome)

# Limpar toda a lista
nomes.clear()
print(nomes)

nomes.append("Wilson")
print(nomes)