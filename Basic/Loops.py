# print() - to print some in console
# print(param,end = "") end="" add something in end of print
# print(f"text{var}") f - format string used to insert variable value in string using {} and var name inside

def for_loop_try():
    for i in range(0,100):
        print(i, end = " ")

def while_loop_try():
    num = 0
    while num != 5:
        num+=1
        print(num)

def string_in_loop():
    string = "test"
    for c in string:
        print(c)

# else in loop executes instruction(s) after all loop iterations 
def string_in_loop_else():
    string = "test"
    for c in string:
        print(c)
    else:
        print("Done")

def nested_while_loop():
    i = 1
    j = 1
    while i != 10:
        while j != 10:
            print (i*j, end= "\t")
            j+=1
        print("\n")
        j = 1
        i += 1

nested_while_loop()