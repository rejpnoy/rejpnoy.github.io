lst = [1, 2, 3, 4, 5, 6]
x = 42
def sum_odd_and_even(lst):
    print("HELLO")

    for i in lst:
        if(i % 2 == 0):
            print(str(i) + " EVEN")
            # Now ADD IT 
            
           # addSumEven = int(i)
            #addSumEven = sum(i)
         
           # print(addSumEven, "TOTAL SUM")
        else:
            print(type(i))
            print(str(i) + " ODD")
            

           # addSumOdd = int(i)
           # addSumOdd = sum(i)
           # print(addSumOdd, "TOTAL SUM")
        
  

    return 


sum_odd_and_even(lst)