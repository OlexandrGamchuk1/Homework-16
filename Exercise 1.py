def geometric_progressions(start, stop, multiplier):
    while start < stop:
        product = start * multiplier
        if product == 'exit':
            exit()
        else:
            yield product
        start *= multiplier


g = geometric_progressions(2, 6, 2)
print(next(g))
g.send('exit')
print(next(g))