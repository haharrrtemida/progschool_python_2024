# написать программу, которая определяет являются ли две строки анаграммами
text = input ('Введите первую строку:  ') 
text_1 = input ('Введите вторую строку:   ')
text_s_1 = sorted(text.lower().replace(' ', '')) 
text_s_2 = sorted(text_1.lower().replace(' ', '')) 
if text_s_1 == text_s_2:
    print (f'{text} и {text_1} являются анаграммами')
else:
    print ('Это не анаграммы!')

