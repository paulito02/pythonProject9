def highest_even(li):
    evens = []
    for x in li:
        if x % 2 ==0:
            evens.append(x)
    return max(evens) 
print(highest_even([2,10,2,3,4,8,11]))