# наша задача не допустить отрицательной скидки

def apply_discount(product, discount):
    """ продукт на вход приходит в виде словаря, а функция возвращает его имя и скидку"""
    price = int(product['цена'] * (1.0 - discount))
    try:
        assert 0 <= price <= product['цена']
    except AssertionError:
        print("Протри глаза! ")
    else:
        data = product['имя'] +" "+ product['страна'] +" " +str(price)
        return data

kreslo = {'имя': 'кресло', 'цена' : 1200,  'страна': "China"}

print(apply_discount(kreslo, 0.25))


print(apply_discount(kreslo, 2.5))
