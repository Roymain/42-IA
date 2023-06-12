
import numpy as np
from PIL import Image
import tornado


def ft_invert(array) -> np.array:
    res = []
    for x in array:
        for i in x:
            res.append([255 - i[0], 255 - i[1], 255 - i[2]])
    final = np.asarray(res).astype(np.uint8)
    final = final.reshape(257, 450, 3)

    return final


ft_invert.__doc__ = "apply inverted filter"


def ft_red(array) -> np.array:
    res = []
    for x in array:
        for i in x:
            res.append([i[0], 0, 0])
    final = np.asarray(res).astype(np.uint8)
    final = final.reshape(257, 450, 3)

    return final


ft_red.__doc__ = "apply red filter"


def ft_green(array) -> np.array:
    res = []
    for x in array:
        for i in x:
            res.append([0, i[0], 0])
    final = np.asarray(res).astype(np.uint8)
    final = final.reshape(257, 450, 3)

    return final


ft_green.__doc__ = "apply green filter"


def ft_blue(array) -> np.array:
    res = []
    for x in array:
        for i in x:
            res.append([0, 0, i[0]])
    final = np.asarray(res).astype(np.uint8)
    final = final.reshape(257, 450, 3)

    return final


ft_blue.__doc__ = "apply blue filter"


def ft_grey(array) -> np.array:

    res = np.dot(array[..., :3], [0.2989, 0.5870, 0.1140])
    final = np.asarray(res)
    test = Image.fromarray(final)

    return test


ft_grey.__doc__ = "apply grey filter"
