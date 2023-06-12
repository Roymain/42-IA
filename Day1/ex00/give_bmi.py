
def give_bmi(height: list[int | float], weight: list[int | float])\
 -> list[int | float]:
    assert all([isinstance(height, list), isinstance(weight, list), ]),\
     "not a list"
    assert all(([isinstance(elem, int)
                or isinstance(elem, float) for elem in height])), \
        "height list doesnt contain int or float "
    assert all(([isinstance(elem, int)
                or isinstance(elem, float) for elem in weight])), \
        "weight list doesnt contain int or float "
    assert len(height) == len(weight), "height list and weight\
     list aren t the same size"

    return [j / (i ** 2) for i, j in zip(height, weight)]


give_bmi.__doc__ = "return a list of bmi"


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    assert isinstance(bmi, list), "bmi isn t a list"
    assert isinstance(limit, int), "limit isn t integer"

    return [int(x) > limit for x in bmi]


apply_limit.__doc__ = "return a list of booleen, true when bmi >\
 limit and false if not"
