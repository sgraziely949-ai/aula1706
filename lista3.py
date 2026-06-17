# excluir pelo valor
pecas = ["Retrovisor", "volante", "Buzina", "Pedais", "Pastilha de freio", "Bomba de água"]
for pecas in pecas:
    print(pecas)
pecas.remove("Buzina")
print(pecas)

pecas.pop(0)
print(pecas)

del pecas[1]
print(pecas)