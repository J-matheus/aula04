num = int (input(f"informe o número: "))
print("os numeros impares sao: ",end="")
for i in range (1,num + 1):
    if i % 2 == 1:
        print(f"{i},",end=" ")
