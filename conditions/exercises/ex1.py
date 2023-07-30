Nome = input("What's your name? ")

print("Welcome", Nome)

OK = input("How are you doing? 1. I'm good, 2. Not so well ")

if OK == '1':
    print("Awesome")
else:
    print("Ohh, what a pity")

Idade = input("By the way, how old are you? ")

N_Idade = int(Idade)

if N_Idade < 10:
    print("So young! ")
elif N_Idade > 10 and N_Idade < 18:
    print("You're young! ")
else: 
    print("Don't worry, you're still young haha")
    
N1 = input("Now, type a ramdom number ")
N2 = input("Again: ")
N3 = input("Again: ")

print("OK")

Number1 = float(N1)
Number2 = float(N2)
Number3 = float(N3)

if Number1 > Number2 and Number1 > Number3:
    print("O maior número é:", Number1)
elif Number2 > Number1 and Number2 > Number3:
    print("O maior número é:", Number2)
else:
    print("O maior número é:",Number3)
if Number1 < Number2 and Number1 < Number3:
    print("O menor número é:", Number1)
elif Number2 < Number1 and Number2 < Number3:
    print("O menor número é:", Number2)
else:
    print("O menor número é:",Number3)
    