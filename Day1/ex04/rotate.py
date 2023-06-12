from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib
import tornado


def main():
    matplotlib.use('webagg')
    try:
        ret = ft_load("animal.jpeg")
        img2_arr = ret[100:500, 450:850, :]
        img2_arr = np.dot(img2_arr[..., :3], [0.2989, 0.5870, 0.1140])
        ro_arr = np.asarray(list(list(x) for x in zip(*img2_arr))[::1])
        img2 = Image.fromarray(ro_arr)

        print("New shape after Transpose: (400, 400)")
        print(ro_arr)

        plt.imshow(img2)
        plt.show()

    except AssertionError as msg:
        print(msg)


main.__doc__ = "load an image, put it in B&W then rotate it"


if __name__ == "__main__":
    main()
