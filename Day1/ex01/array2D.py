import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    assert all([isinstance(start, int),
                isinstance(end, int), isinstance(family, list)]),\
         "instances doesnt correspond to proto"
    assert len(np.shape(family)) == 2, "not a 2D array"
    print("my shape is :", np.shape(family))

    tmp = family[start:end]

    print("my new shape is :", np.shape(tmp))
    return tmp


slice_me.__doc__ = "slice list with start and end args"
