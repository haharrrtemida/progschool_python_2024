"""
По данному натуральному n ≤ 9 выведите лесенку из n ступенек,
i-я ступенька состоит из чисел от 1 до i без пробелов.

    1 1
   21 12
  321 123
 4321 1234
54321 12345
"""

n = int(input("n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(j + 1, end = "")
    print()