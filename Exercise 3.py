def numbers(n):
    i = 1
    while i <= n:
        number = 0
        j = 1
        while j <= n:
            if i % j == 0:
                number += 1
            j += 1
        if number == 2:
            yield i
        i += 1


for number in numbers(10):
    print(number)