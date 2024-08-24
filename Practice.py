def nested_while_loop(numbers):

    i = 0
    while i != numbers+1:
#        print(str(i).zfill(len(str(numbers))), end=" ")
        print(my_own_rjust(str(i),len(str(numbers)),"0"), end=" ")
        i += 1
    
    
def my_own_rjust(string, count, fill):

    i=[]

    for a in range(0,count-len(string)):
        i.append(fill)

    for c in string:
        i.append(c)

    return ''.join(i)

print(my_own_rjust("string", 7, "#"))