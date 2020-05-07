# наша задача не допустить отрицательной скидки

def apply_discount(product, discount):
    """ продукт на вход приходит в виде словаря, а функция возвращает его имя и скидку"""
    data=[]
    for key,value in product.items():
        for one_value in discount:
            price = round(float(float(value) * (1.0 - one_value)),2)
            try:
                assert 0 <= price <= float(value)
            except AssertionError:
                data.append("Протри глаза! ")
            else:
                data.append(key +" " +str(price))
    return data

name_of_datafile = 'data.txt'
name_of_discountfile = 'discount.txt'
with open(name_of_datafile) as file_data:
    lines_datafile = file_data.readlines()
with open(name_of_discountfile) as file_discount:
    lines_discountfile = file_discount.readlines()
data_dict = {}
for line_datafile in lines_datafile:
    temp_line=line_datafile.rstrip().split(',')
    data_dict[temp_line[0]]=temp_line[1]

data_discont =[]
for line_discountfile in lines_discountfile:
    data_discont.append(float(line_discountfile.rstrip()))

result = apply_discount(data_dict, data_discont)

result_file = 'result.txt'
with open(result_file, 'w') as file:
    for one_item in result:
        file.write(str(one_item)+'\n')


