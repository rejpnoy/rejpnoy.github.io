# This will calculate the amount of weights in a bar for lifting 
#Rommel Enriquez 

print("Your name?")
lifter = input()
print("Lifter's name: " + lifter.upper())


def plates():
    #inputs in the list of what the lifter puts in. and x times that by 2 
    print("how heavy is the bar?: ")
    barweight = int(input())
    if barweight == 35:
        print("How many plates on 1 side?: ")
        plates_list = []
        n = int(input("How many plates on 1 side?: "))

        

        for i in range(0, n):
            ele = int(input())
            plates_list.append(ele)

        
    return plates_list

print(plates())
