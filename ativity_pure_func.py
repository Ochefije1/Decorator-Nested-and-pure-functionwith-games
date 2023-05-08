# #write a function that will take two argument and return the addition 
# def addition(a, b):
#     return a + b
# result = addition(7, 3)
# print(result)

# #generate a list using the output from the first function
# def addition(a, b):
#     return a + b
# result_list = [addition(4, 1), addition(9, 5), addition(4, 7), addition(3, 6)]
# print(result_list) 

# #return the length of the list and the cumulative of the original list



# #write a function that will take two argument and return the addition 
def add(x:int, y:int)->int:
    """Adds two integers"""
    return x + y

# #generate a list using the output from the first function
def genList(total:int)->list:
    """Returns a list of number range"""
    return list (range(total))

# #return the length of the list and the cumulative of the original list
def cumList(items:list)->tuple([int, list]):
    """Get the cummulative values of a list"""
    cum = []
    for index, item in enumerate(items):
        sm = sum(items[:index + 1])
        cum.append(sm)
        return len(cum), cum


def divCum(x:int, y:int)-> int:
    total = add(x, y)
    print(total)
    items = genList(total)
    print(items)
    length, cum = cumList(items)
    print(length, cum)
    return sum(cum) //length


lastInt = divCum(2, 3)
print(lastInt)


    #generate two aphabet