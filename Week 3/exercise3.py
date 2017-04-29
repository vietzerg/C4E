#COMBINED DICTIONARY

shop = {
    'banana':{
        'price':4,
        'stock': 6},
    'apple':{
        'price': 2,
        'stock': 0},
    'orange':{
        'price': 1.5,
        'stock': 32},
    'pear':{
        'price': 3,
        'stock': 15}
    }

food_list = ["banana", "orange", "apple"]

def compute_bill(foodlist):
    total = 0

    for food in foodlist:
        if shop[food]['stock'] > 0:
            total += shop[food]['price']
            shop[food]['stock'] -= 1
    return total, shop

print (compute_bill(food_list))
