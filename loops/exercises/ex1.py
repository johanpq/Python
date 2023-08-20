Value1 = input("Type the first number: ")
Value2 = input("Type the second number ")

N1 = int(Value1)
N2 = int(Value2)

Even = 0
Odd = 0

for N1 in range(N2):
    if N1 % 2 == 0:
        Even+= N1
    else:
        Odd+= N1

print("The sum of even numbers is:", Even)
print("The sum of odd numbers is", Odd)

amount_even_numbers = 0
amount_odd_numbers = 0

for N1 in range(N2):
    if N1 % 2 == 0:
        amount_even_numbers+= 1
    else:
        amount_odd_numbers+= 1

print("The amount of even numbers is:", amount_even_numbers)
print("The amount of odd numbers is:", amount_odd_numbers)