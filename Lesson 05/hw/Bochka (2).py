barrels_count = int(input('Введите число бочек: '))
last_digit = barrels_count % 10
two_last_digit = barrels_count % 100
result = ""


if two_last_digit >= 5 and two_last_digit <= 20:
    result = "бочек"
elif last_digit == 1:
    result = "бочка"
elif last_digit >= 2 and last_digit <= 4:
    result = "бочки"

print(f'{barrels_count} {result}')