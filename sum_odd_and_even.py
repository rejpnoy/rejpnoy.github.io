lst = [1, 2, 3, 4, 5, 6]
x = 42
def sum_odd_and_even(lst):
    print("HELLO")

    for i in lst:
        if(i % 2 == 0):
            print(str(i) + " EVEN")
            # Now ADD IT 
            addSumEven = sum(lst)
         
            print(addSumEven + "TOTAL SUM")
        else:
            print(str(i) + " ODD")
            print(type(i))
            addSumOdd = sum(lst)
          
            print(addSumOdd + "TOTAL SUM")


    return 


sum_odd_and_even(lst)