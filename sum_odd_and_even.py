lst = [1, 2, 3, 4, 5, 6]
lst2 = [-1, -2, -3, -4, -5, -6]
lst3 = [0, 0]

def sum_odd_and_even1(lst):
    odd_sum = 0 
    even_sum = 0 

    for i  in lst:
        
        print(type(lst))
        if(i % 2 ==  0):
            #EVEN Numbers
            print(type(i))
            print(str(i) + " This is an EVEN Number")
            print(type(even_sum))
            even_sum = even_sum + i        
        else:
            #ODD Numbers
            print(str(i) + " This is an ODD Number")
            odd_sum = odd_sum + i
    print("Total of Even and Total of Odd")
    print(even_sum,odd_sum)
    return [even_sum,odd_sum]
          
sum_odd_and_even1(lst)

