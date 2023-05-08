

# """
# NO 1
# """
# def addition(x, y):
#     return x + y


# sum = addition(5, 10)
# print(sum) 

# # print(addition(2, 3))  


# """
# NO 2
# """
# my_list = []
# my_list.append(sum)

# print(my_list)

# print(len(my_list))


# """
# NO 3

# """
# # my_list = [1, 2, 3, 4, 5]
# # cumulative_sum = []
# # total = 0

# # for i in my_list:
# #     total += i
# #     cumulative_sum.append(total)

# # print(cumulative_sum)



# """
# NO 4

# """
# print((sum)/(len(my_list)))




def add(x:int, y:int)->int:
    """Adds two integers"""
    return x + y


def genList(total:int)->list:
    """Returns a list of number range"""
    return list(range(total))


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
    return sum(cum) // length

lastInt = divCum(2, 3)
print(lastInt)