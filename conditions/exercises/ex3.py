n1 = int(input("Digite o número 1: "))

n2 = int(input("Digite o número 2: "))

n3 = int(input("Digite o número 3: "))

maiorNumero = 0
menorNumero  = 0
""" Maior """
if n1 > n2 and n1 > n3:
    maiorNumero = n1
elif n2 > n3:
    maiorNumero = n2
else:
    maiorNumero = n3
""" Menor """
if n1 < n2 and n1 < n3:
    menorNumero = n1
elif n2 < n3:
    menorNumero = n2
else:
    menorNumero = n3

print("Maior número: ", maiorNumero)
print("Menor número: ", menorNumero)