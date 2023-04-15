rows=int(input("Enter row number:"))
columns=int(input("Enter column number:"))
symbol=input("Enter column number:")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print("", end="\n")