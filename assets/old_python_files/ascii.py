# Credit Comment

# The code in this file is taken from the following walkthrough tutorial:

# https://youtu.be/v_raWlX7tZY?t=63
# Turn any image into ASCII art! (Easy Python PIL Tutorial)

import PIL.Image

# ascii characters used to build the output text

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


# resize image to new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)


# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)


# convert pixels to a string of ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)


def main(new_width=100):
    # https://docs.python.org/3/library/exceptions.html#ImportError
    path = input("Enter pathname to an image:\n")
    try:
        image = PIL.Image.open(path)
    except ImportError:
        print(path, "is not a valid pathname to an image.")

    # convert image to ASCII
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    # split image into parts
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for
                            i in range(0, pixel_count, new_width))

    # print result
    print(ascii_image)

    # save result to "ascii_image.txt"
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)


main()
