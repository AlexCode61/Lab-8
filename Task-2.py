from random import *

class value_error(Exception):
    pass

def IsPowerN(k:int,n:int):
    while k >= n:
        if (k % n) != 0:
            return False
        else:
            k = k // n
    if k == 1:
        return True
    else:
        return False

def input_chek(string:str):
    while True:    
        try:
            value = int(input(string))
            if value < 2:
                raise value_error
            break
        except ValueError:
            print('ERROR-0\nВведено не целое число')
        except value_error:
            print('ERROR-1\nВведенно отрицательное число')
    return value

n = input_chek('Введите число: ')

list_k = [randint(0,99) for _ in range(10)]

for val in list_k:
    if IsPowerN(val,n):
        print(f'{val} является степенью числа {n}')
    else:
        print(f'{val} не является степенью числа {n}')