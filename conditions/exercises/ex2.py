Currency = input("What type of currency you'd like converting? 1. Dolar to Real | 2. Real to Dolar ")

Number = float(Currency)

if Number == 1:
    Value = input("Type the value: ")
    Value_n = float(Value)
    
    Result = Value_n * 4.78
    print("It's:", Result)
elif Number == 2:
    Value = input("Type the value: ")
    Value_n = float(Value)

    Result = Value_n / 4.78
    print("It's", Result)
else:
    print("It wasn't possible to convert, try it again")


#on 07.22.23 the dolar was 4.78

