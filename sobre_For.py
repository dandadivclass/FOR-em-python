#o loop FOR é usado para navegar repetidamente por grandes números de dados, como string, listas, tuplas, dicionários etc

for letra in 'olá':     #para -itens- em 'string' faça algo     #o -item- pode ser descrito como qualquer coisa!
    print(letra)            #imprime item um por um

listinha = ['a', 'e', 'i', 'o', 'u']
for letras in listinha:         #para -itens- em lista faça algo
    print(letras)
    if letras == 'o':               #se -item- for igual a 'item da lista':
        break                           #pare

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue        #se -item- for igual a -item da lista- continue com o próximo looping
  print(i)


for x in range(4):      #a função range dá um valor a ser repetido o loop for
    print(x)

for i in range(10, 20):     #recebe dois valores como parâmetro inicial e parâmetro final
    print(i)
else:                           #quando a condição não for mais verdadeira execute o else
    print("Acabou o looping")

for b in range(20, 40, 2):      #e também 3 valores, o último é o parâmetro incremento (quantas casas serão puladas)
    print(b)
