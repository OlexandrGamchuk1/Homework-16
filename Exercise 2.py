def generator(start, stop, step=1):
    while start < stop:
        yield start
        start += step
    while start > stop:
        yield start
        start -= step


print(list(generator(150, 0, 4)))
print(list(generator(2, 10, 1)))