'''Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения start включительно до величины end включительно.
 Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.'''
def sum_range(start, end):
    index = start
    result = 0
    while index <= end:
        result += index
        index += 1
    return result


start = int(input('Введите параметр start: '))
end = int(input('Введите параметр end: '))
if start > end:
    start, end = end, start
result = 0
result = sum_range(start, end)
print(f'Сумма чисел от {start} до {end} = {result}')    