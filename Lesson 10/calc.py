def add(first, second):
    return first + second

def sub(first, second):
    return first - second

def multi(first, second):
    return first * second

def div(first : int, second : int) -> float:
    return first / second

first = int(input("A: "))
sign = input("sign: ")
second = int(input("B: "))
result = 0
match sign:
    case "+":
        result = add(first, second)
    case "-":
        result = sub(first, second)
    case "*":
        result = multi(first, second)
    case "/":
        result = div(first, second)
print(result)

# 2 + 2 * 2
# result = add(2, multi(2, 2))
# print(result)