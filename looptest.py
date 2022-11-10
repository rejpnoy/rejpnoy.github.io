# pyramid = 10
# for i in range(0, pyramid):
#     for j in range(0, pyramid-i):
#         print("", end="")
#     for k in range(0, 2 * i + 1):
#         print("0", end="")
#     print("")

row = int(input("Enter Number of rows: "))
for  i in range(row):
    for j in range(i+1):
        print("0 ", end="")
    
    
    print("\n")


rows = 10

k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()