f = lambda x: x ** 2
g = lambda x: (1 / 3) * x ** 3
limits = (0, 5)
resolution = (20, 20)


def integrate(func, lim, res):
    scale_x = lim[1] / res[0]
    scale_y = func(lim[1]) / res[1]
    array = []
    for x in range(0, res[0]):
        array.append([0] * res[1])
    for index_x, x in enumerate(array):
        for index_y, y in enumerate(x):
            if func(index_x * scale_x) >= index_y*scale_y:
                array[index_x][index_y] = 1
    area_sum = sum(x.count(1) for x in array)
    result = area_sum*scale_y*scale_x
    return result


print(integrate(f, limits, resolution))
print(g(limits[1]))
