def table():
    print('  F   ',' C')
    formatStr = '{0:5.1f} {0:5.1f}'
    for num in range(-30, 50, 10):
        print(formatStr.format(convert(num),num))
    return


def convert(celsius):
    return celsius * 1.8 + 32


print(table())
