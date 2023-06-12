import math


def NULL_not_found(object: any) -> int:
    if type(object) == str and object != "":
        print("Type not found")
        return 1
    if object is None:
        print("Nothing: ", end='')
    if type(object) == int and type(object) != False:
        if object == 0:
            print("Zero: ", end='')
            print(object, type(object))
            return 0
        else:
            return 0
    if object == "":
        print("Empty: ", end='')
    if type(object) == bool:
        if object == False:
            print("Fake: ", end='')
        else:
            return 0
    if type(object) == float:
        if object == 0:
            print("Cheese: ", end='')
        else:
            return 0
    print(object, type(object))

    return 0