# while (ПОКА) 
# while условие:
#     тело
#     конструкции

# a = 'а'

# while a < 'z':
#     a = chr(ord(a) + 1)
#     print(a)


a = 0 

while True:
    a += 1
    if a == 5:
        continue
    if a == 10:
        break
    print(a)