stop = True
while stop:
    operate = input("Введите операцию (+,-,*,/,**,//,%)")
    if operate == "stop":  # остановка калькулятора
        stop = False
        break
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    c = 1.0
    if operate == "+": # плюс
        c = float(a) + float(b)
    elif operate == "-": # минус
        c = float(a) - float(b)
    elif operate == "*": # умножение
        c = float(a) * float(b)
    elif operate == "/": # деление
        c = float(a) / float(b)
    elif operate == "**": # возведение в степень
        c = float(a) ** float(b)
    elif operate == "//": # деление без остатка
        c = float(a) // float(b)
    elif operate == "%": # остаток от деления
        c = float(a) % float(b)
    else:
        print("неправильная операция")
    print("Ответ: " + str(c))
