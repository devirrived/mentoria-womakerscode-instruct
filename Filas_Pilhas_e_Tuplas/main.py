# pilha: último que entra, primeiro que sai 

pilha = []

pilha.append(1)
pilha.append(2)
pilha.append(3)
pilha.pop()

print(pilha)

# fila: primeiro que entra, primeiro que sai 

fila = []

fila.append(1)
fila.append(2)
fila.append(3)
del fila[0]

print(fila)

tupla = (1, 2, 3, 4) #Tupla é uma estrutura de dados IMUTÁVEL
print(tupla)

tupla.append(1)
print(tupla)
