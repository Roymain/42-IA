from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib
import tornado


def main():
    matplotlib.use('webagg')
    try:
        ret = ft_load("animal.jpg")
        img2_arr = ret[100:500, 450:850, :]

        res = np.dot(img2_arr[..., :3], [0.2989, 0.5870, 0.1140])
        final = np.asarray(res)
        img2 = Image.fromarray(final)
        last_arr = np.asarray(img2)

        print("New shape after slicing: (", img2.size[1], ", ",
              img2.size[0], ", ", len(img2.mode), ") or (",
              img2.size[1], ", ", img2.size[0], ")\n", end='', sep='')
        print(last_arr)
        plt.imshow(img2)
        plt.show()

    except AssertionError as msg:
        print(msg)


ft_load.__doc__ = "load an image, print its formatt,\
 and its pixels content in a RGB format"


if __name__ == "__main__":
    main()
