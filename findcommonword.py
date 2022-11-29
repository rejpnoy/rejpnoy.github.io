
#my_list  = [1, 2, 3]
#double = [item * 2 for item in my_list]
#for item in my_list:
#    double.append(item *2)
#print(double)

#username_list = [user['name'] for user in users]

# a = 1, 2, 3, ,4, ,5
# i =+ 1
# i =-

ex ="Rommel is a global investment management firm that " \
    "utilizes a diversified portfolio of Rommel and quantitative " \
    "strategies across financial markets that Rommel to achieve high quality, " \
    "uncorrelated returns for our clients."
# first step is converting variable string into 1 string hence 1 array index of 0


my_list  = [ex]

print(my_list)

dict = {}
mystring = " "
count, itm = 0, ''

# need to lowercase all strings in the array
# for loop gets the range
for i in range(len(my_list)):
    print(my_list)
    #lower casses
    #replace method = replaces . with empty string
    my_list[i] = my_list[i].lower().replace('.','').replace(',','')
    print(my_list)
    #This puts a list into a variable string
    for x in my_list:
        mystring += " " + x
        #now need to convery from string to list again by split method.
        convert = mystring.split()
        print(convert)

        for item in reversed(convert):
            dict[item] = dict.get(item, 0) + 1
            if dict[item] >= count:
                count, itm = dict[item], item
        print(dict)









