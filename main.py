# list methpds in python

basket = [1,2,3,4,5]
new_list=basket.append(6)
print(basket)
basket.insert(4,8)
print(basket)
basket.extend([9,10,11])
print (basket)
basket.pop()
print(basket)
basket.remove(4)
print(basket)
basket.remove(2)
print(basket)
print(basket.index(3))
print(8 in basket)
print('8' in basket)
print(basket.count(6))
print(basket.sort())
basket.sort()
print(basket)
print(sorted(basket))
# sorted doesnt sort the basket it create a new array thats is sorted
new_basket=basket.copy()
basket.reverse()
print(basket)
basket[::-1]
basket.reverse()
print(basket)

#  unpacking

a,b,c =[1,2,3]
print(a)
print(b)
print(c)

a,b,c, *other,d = [1,2,3,4,5,6,7,8]
print(a)
print(b)
print(c)
print(other)
print(d)













