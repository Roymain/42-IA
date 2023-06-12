
def all_thing_is_obj(object: any) -> int:
    if not object:
        return 42
    if type(object) == float or type(object) == int:
        print("Type not found")
        return 42
    if type(object) == str:
        print(object + " is in the kitchen : ", end='')
        print(type(object))
        return 42
    strg = str(type(object))
    strg = strg[8:len(strg) - 2]
    strg = strg.capitalize()
    print(strg , ": ", end='')
    print(type(object))

    return 42


