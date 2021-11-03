def pyramid(n):
    # if we get a pring of size 5 and incleease of line 
    for i in  range(n):
        line_to_print = "o"
        for j in range(i):
            line_to_print += "o"
        print(line_to_print)
    return

pyramid(5)
