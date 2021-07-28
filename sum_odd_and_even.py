lst = [1, 2, 3, 4, 5, 6]
x = 42
def sum_odd_and_even(lst):
    print("HELLO")

    for i in lst:
        if(i % 2 == 0):
            print(str(i) + " EVEN")
            # Now ADD IT 
            addSum = sum(i)
            print(addSum + "TOTAL SUM")
        else:
            print(str(i) + " ODD")
            addSum = sum(i)
            print(addSum + "TOTAL SUM")


    return 


sum_odd_and_even(lst)