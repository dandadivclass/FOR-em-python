#Faça um programa que leia 5 números e informe a soma e a média dos números.

lista_numeros = []
for i in range(5):
    numero = lista_numeros.append(int(input("Digite seu numero")))
    soma = sum(lista_numeros)
    media = soma / 5

print(soma)
print(media)
