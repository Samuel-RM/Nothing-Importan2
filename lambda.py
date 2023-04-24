# hola = 22
# lambda x : x * 3

# hola2 = (lambda x : x * 3)(hola)

# print(hola2)
"""Tenemos una lista con un conjunto de diccionarios dentro"""
items = [
 {
    'products': 'CAmisa',
    'price': 100
 },
 {
    'products': 'pantalones',
    'price': 1400
 },
 { 
    'products': 'zapatos',
    'price': 10220
    }
]

"""COn las funcione lambda y map y list, buscaremos los valores de la lista , y veremos como 
funciona map y veremos como agregar un valir key a los diccionarios """
prices = list(map(lambda item : item['price'], items ))
print(prices)

price2 = list(map(lambda item : item['products'] , items))
print(price2)

nex_items = list(map(lambda item: item['price'] * 0.19 , items))
print(nex_items)


def add_taxes(item):
    item['taxe'] = item['price'] * 0.19
    return item 

nex_items2 = list(map(add_taxes, items))
print(nex_items2)

'''con la funcion map en una lista de diccionarios se puede transformar la lista
agregando items nuevos como  por ejemplo seria incluirle impuestos, tambien se usa la 
funcion map con las funciones normales cuando las lambdas ya no son suficiente'''

