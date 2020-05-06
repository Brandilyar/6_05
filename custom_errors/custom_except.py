day = int(input("Введите, какой сейчас день? "))
try:
    if day > 31:
        raise ValueError(" Слишком большое число")
except ValueError as msg:
    # exit()
    print("Программа нашла", msg)
else:
    print(f"Классная погода {day} числа")

# finally:
