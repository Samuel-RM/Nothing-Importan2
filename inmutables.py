items = [
 {
    'products': 'Camisa',
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

def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * 0.19
    return new_item

new_items = list(map(add_taxes, items))
print(new_items)

print('NEW LIST')
print(new_items)
print()
print('OLD LIST')
print(items)