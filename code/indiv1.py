from module import fun1

if __name__ == "__main__":
    a = int(input("введите а "))
    b = int(input("введите b "))
    test_fun = fun1()
    print("Для значений a, b функция f'(a,b) =", test_fun(a, b))