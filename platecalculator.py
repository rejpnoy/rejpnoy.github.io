# This will calculate the amount of weights in a bar for lifting
# Rommel Enriquez

print("Your name?")
lifter = input()
print("Lifter's name: " + lifter.upper())


def weightrecord(name, weight_rec):

    dict = {}
    dict.update({name:weight_rec})
    for i in dict.items():

        print("Weight of this has been added to the dictionary list")
        print(i)
         
    
    print(dict)
    return dict



def plates():
    # inputs in the list of what the lifter puts in. and x times that by 2
    print("how heavy is the bar?: ")
    bar_weight = int(input())
    if bar_weight == 35:

        plates_list = []

        n = int(input("How many plates on 1 side?: "))
        print("What is the weight per pounds for each plates: ")

        for i in range(0, n):
            #in for loop

            ele = int(input())
            # adds the plated input into the list of elements
            plates_list.append(ele)

        #out of for loop
        # gives me the total from the plates_list
        print("total of the plates: ")
        totalweight = sum(plates_list) * 2 + 35
        print("congrats! " + lifter + " you just repped " + str(totalweight))
        weightrecord(lifter,totalweight)

    elif bar_weight == 45:
        
        plates_list = []

        n = int(input("How many plates on 1 side?: "))
        print("What is the weight per pounds for each plates: ")

        for i in range(0, n):
            #in for loop

            ele = int(input())
            # adds the plated input into the list of elements
            plates_list.append(ele)

        #out of for loop
        # gives me the total from the plates_list
        print("total of the plates: ")
        print(sum(plates_list) * 2 + 45)
    else: 
        print("Incorrect barbell weight")
        pass
    return plates_list


plates()
