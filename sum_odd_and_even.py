lst1 = [1, 2, 3, 4, 5, 6]
lst = [-1, -2, -3, -4, -5, -6]
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
    odd_sum = 0 
    even_sum = 0 

    for i  in lst:
        
        print(type(lst))
        if(i % 2 ==  0):
            print(str(i) + " This is an EVEN Number")
            even_sum = even_sum + i        
        else:
            print(str(i) + " This is an EVEN Number")
            odd_sum = odd_sum + i
    print("End Line:")
    print(even_sum,odd_sum)
    return(even_sum,odd_sum)
          
sum_odd_and_even1(lst)

