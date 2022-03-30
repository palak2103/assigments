#Write a function that returns the largest element in a list.
def max_min():
    list = [21,3,4,65,78,9,7,65,45,34,324,6,5]
    listmax,listmin=list[0],list[0]
    for i in list:
        if i>listmax:
            listmax = i
        if i<listmin:
            listmin = i
        print(listmax,listmin)
max_min()                        
