lst2 = [1, 2, 3, 4, 6, 7, 8, 9, 10]
lst = [7, 2, 3, 6, 5, 9, 1, 4, 8]
def missing_num(lst):
    n = len(lst)
    total = (n + 1)*(n + 2)/2
    sum_of_lst = sum(lst)

    return total - sum_of_lst

miss  = missing_num(lst)
print(miss)


def missing_num1(lst):
    print(lst)
    lst.sort()
    print(lst)
    missing_element  = []
    for i in  range(lst[0], lst[-1]+1):
        if i not in lst:
            missing_element.append(i)
    
    return [missing_element]

missing_num1(lst2)