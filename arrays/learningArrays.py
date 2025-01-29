lista = [1, 2, 3]

print(lista[0])
print(lista[1])
print(lista[2])

contador = 0

while contador < 5:
    novoNumero = int(input("Digite um novo número maior do que os que já existem na lista: "))

    """ Max é um função nativa do python que checa se o ńumero é maior """
    if novoNumero > max(lista):
        lista.append(novoNumero)
        contador+= 1 # Incrementa
    else:
        print("Número não é maior!")

    """ for i in range(lista): -> Isso não funciona porque lista não é um número, range só funciona com números """

    """ Igual ao JS, Java, i será os elementos e vai iterar até o último elemento (n-1) do array  """
    for i in lista:
        print(i)