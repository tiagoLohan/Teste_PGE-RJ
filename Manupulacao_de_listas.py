'''
Dado a lista numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3], escreva um código que:

a) Remova os números duplicados, mantendo a ordem original.
b) Retorne a soma de todos os números da lista após a remoção dos duplicados.
'''


numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# a) Remova os números duplicados, mantendo a ordem original.

numeros_tratados = []     # Lista sem duplicados e na ordem da lista original.

#Laço para percorrer a lista numeros e incluir na lista auxiliar apenas 1x.
for num in numeros:
  if num not in numeros_tratados:
    numeros_tratados.append(num)

print(numeros_tratados)


# b) Retorne a soma de todos os números da lista após a remoção dos duplicados.

soma = sum(numeros_tratados)
print(soma)




