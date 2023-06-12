from load_image import ft_load
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_invert
from pimp_image import ft_grey
import matplotlib
import matplotlib.pyplot as plt
import tornado


def main():
    matplotlib.use('webagg')
    try:
        array = ft_load("landscape.jpg")
        fig, axs = plt.subplots(2, 3)
        axs[0, 0].imshow(ft_invert(array))
        axs[0, 1].imshow(ft_red(array))
        axs[0, 2].imshow(ft_green(array))
        axs[1, 0].imshow(ft_blue(array))
        axs[1, 1].imshow(ft_grey(array))
        axs[1, 2].imshow(array)
        plt.show()
        print(ft_invert.__doc__)

    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    main()
