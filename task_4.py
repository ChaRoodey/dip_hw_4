def max_of_2(x, y):
    if x > y:
        return x
    else:
        return y


def max_of_3(x, y, z):
    return max_of_2(max_of_2(x, y), z)


print(max_of_3(5, 15 ,3))