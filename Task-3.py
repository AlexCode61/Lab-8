def function():
    try:
        n = int(input())
        if n == 0:
            return
        elif n % 2 == 1:
            function()
            print('Нечётное число', n)
        else:
            function()
    except:
        print('Введенно не целое число')
function()