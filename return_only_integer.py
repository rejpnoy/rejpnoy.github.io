lst = ([9, 2, "space", "car", "lion", 16])

def return_only_integer(lst):
    x = lst
    for i in  x:
        
        if type(i) == int:
            #print(i , "This is a int")
            return_integer = [i]
            print(return_integer)
    return return_integer


def return_only_integer1(lst):
    new_list = []
    for i in lst:
        
        if type(i) == int:
            
            
            new_list.append(i)
    print(new_list)
    return new_list
return_only_integer1(lst)
