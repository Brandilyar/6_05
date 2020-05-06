print("простой калькулятор")
print("q  to quit")

while True:
    first_num = input("\n Первое число: ")
    if first_num == 'q':
        break
    second_num = input("\n Второе число: ")

    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print(" ошибка деления на ноль")
    else:
        print(answer)
