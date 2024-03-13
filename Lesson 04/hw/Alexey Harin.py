keg = int(input("Какое количество бочек вам нужно? - "))

first_variant = 'бочек'
second_variant = 'бочки'
third_variant = 'бочка'
bulk = 'по оптовой цене'
retail = 'по розничной цене'

if keg == 0:
    print(f'{keg} {first_variant} обойдутся Вам слишком дорого!')
elif keg == 1:
    print(f'{keg} {third_variant} {retail}')
elif keg >= 2 and keg < 5:
    print(f'{keg} {second_variant} {retail}')
elif keg >= 5 and keg <= 20:
    print(f'{keg} {first_variant} {retail}')
elif keg >= 21 and keg <= 999:
    if (keg % 10) >= 2 and (keg % 10) < 5:
        print(f'{keg} {second_variant} {bulk}')
    elif (keg % 10) == 1:
        print(f'{keg} {third_variant} {bulk}')
    else:
        print(f'{keg} {first_variant} {bulk}')
elif keg > 999:
    print('Крупный опт можно склонять как Вам угодно!')
