 #Задание 1. Сумматор
# Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения start
# включительно до величины end включительно. #Если пользователь задаст первое число большее 
# чем второе, просто поменяйте их местами.

def sum_range (start, end):
    numbers = list(range(start, end +1))
    range_sum = sum(numbers)
    return range_sum

          
start = int(input('Enter first number '))
end = int(input('Enter second number  '))
if start > end:   start, end = end, start
print(sum_range (start, end))


#Один банк сделал у Вас заказ: реализовать калькулятор для вкладов. Пользователь вводит сумму вклада в размере n рублей сроком 
#на years  лет под 10% годовых.Написать функцию calculate(), принимающую аргументы n и years и возвращающую сумму, которая будет
# на счету пользователя через years лет.'''

def Calculate (money, years):
    money_incom = money+ money/10*years
    return money_incom

money = int(input('Введите сумму вклада: '))
years = int(input('Cрок вклада: '))
print(f'Через {years} лет сумма на Вашем счете в рублях будет:')
print(Calculate(money, years))