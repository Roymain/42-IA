def callLimit(limit: int):
    '''call limit function'''
    count = 0

    def callLimiter(function):
        '''call limiter function'''

        def limit_function(*args: any, **kwargs: any):
            '''limit  function'''
            nonlocal count
            count += 1
            if count > limit:
                print(f"Error: {function} call too many times")
            else:
                return function(*args, **kwargs)
        return limit_function
    return callLimiter
