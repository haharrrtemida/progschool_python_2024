# 1. Удалите в строке ' a b c   d e f '
# все пробелы и выведите результат на экран

input_data_1 = ' a b c   d e f '
output_data_1 = input_data_1.replace(' ', '')

print(output_data_1)

# 2. Дана строка '131231442145'.
# Подсчитайте в ней количество символов '1' и выведите результат на экран.

input_data_2 = '131231442145'
output_data_2 = input_data_2.count('1')

print(output_data_2)

# 3*. Написать программу, которая сможет определить,
# являются ли две строки анаграммами

input_data_3, input_data_4 = 'кабан', 'банка'
output_data_3, output_data_4 = sorted(input_data_3), sorted(input_data_4)
comparison = output_data_3 == output_data_4

print(comparison)
