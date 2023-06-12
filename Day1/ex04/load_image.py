from PIL import Image
import numpy as np
import os.path


def ft_load(path: str) -> np.array:
    assert isinstance(path, str), "path isn t a string"
    assert ".jpeg" in path or ".jpg" in path, "format not handle"
    assert os.path.exists(path), "path doent exist"
    img = Image.open(path)
    img_arr = np.asarray(img)
    print("The shape of image is: (", img.size[1],
          ", ", img.size[0], ", ", len(img.mode), ")", end='', sep='')
    print("\n", end='')
    print(img_arr)

    return img_arr


ft_load.__doc__ = "load an image, print its formatt,\
 and its pixels content in a RGB format"
