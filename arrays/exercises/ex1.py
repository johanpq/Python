notas = []

sair = False

contador = 1

while sair == False:
    n1 = int(input("Nota 1: "))
    n2 = int(input("Nota 2: "))
    n3 = int(input("Nota 3: "))

    querSair = int(input("Deseja sair? 0-> Sim | 1-> Não "))
    if querSair == 0:
        sair = True
    else:
        sair = False
    
    notas.append(n1)
    notas.append(n2)
    notas.append(n3)
    notas.sort()

for i in notas:
    print("Nota ", contador, ": ", i)
    contador+= 1