from load_image import ft_load


def main():
    try:
        print(ft_load("landscape.jpg"))

    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    main()
