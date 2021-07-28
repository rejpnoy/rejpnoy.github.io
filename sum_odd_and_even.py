lst = [1, 2, 3, 4, 5, 6]
x = 42
def sum_odd_and_even(lst):
    print("HELLO")
    length  = len(lst)
    for i in lst:
        if(i % 2 == 0):
            addSum = i
            print(str(i) + " EVEN")
            addSum = sum(length)
        
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

def sum_odd_and_even1(lst):

    if(lst % 2 ==  0):
        print(str(lst) + "EVEN")
    else:
        print(str(lst) + "ODD")
    
sum_odd_and_even1(lst)