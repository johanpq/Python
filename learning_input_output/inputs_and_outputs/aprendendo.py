print("Hellow World") #printar na tela

x = 4 #declaracao de variável, não precisa especificar o tipo

x = 10

print(x)

x = "Meu nome é: " #string

print(x) 

Nome = input("Digite seu nome: ")  #usario digitar, e armazena na variavel

print("O nome digitado foi", Nome)

#todo valor armezenado no input é string
#para utilizar numeros, é necessário converter (igual o JS)

x = input("Digite um número: ")
y = input("Digite um numero: ")

x_n1 = int(x)  #float() para float
y_n2 = int(x) 

soma = x_n1 + y_n2

print("A soma de", x_n1, "e", y_n2, "é:", soma)