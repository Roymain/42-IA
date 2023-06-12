
def ft_filter(fct, iterable):
    if not fct:
        res = [x for x in iterable if x is True]
        return iter(res)
    res = [x for x in iterable if fct(x) is True]
    return iter(res)


ft_filter.__doc__ = "ft_filter(function or None, iterable) --> \
filter object \n\n\
Return an iterator yielding those items of iterable for which function(item)\n\
is true. If function is None, return the items that are true."
