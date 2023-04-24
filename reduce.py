import functools

list = [1, 2, 3, 4]

def accum(acoun, item):

    print('this is the counter ==> ', acoun)
    print('this is the item ==>', item)
    
    return acoun + item
  
result2 = functools.reduce(accum ,list)
print(result2)
# result = functools.reduce(lambda counter, item: counter + item, list )
# print(result) 