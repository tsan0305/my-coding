"""
File: stanCodoshop.py
Name: 林贊
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    color_distance = ((red-pixel.red)**2 + (green-pixel.green)**2+(blue-pixel.blue)**2)**0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    r_total = 0   # the total red values of the pixels
    g_total = 0   # the total green values of the pixels
    b_total = 0   # the total blue values of the pixels
    for pix in pixels:
        r_total += pix.red
        g_total += pix.green
        b_total += pix.blue
    r_agv = r_total // len(pixels)
    g_agv = g_total // len(pixels)
    b_agv = b_total // len(pixels)
    rgb_agv = [r_agv, g_agv, b_agv]
    return rgb_agv


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    rgb_agv = get_average(pixels)
    r = rgb_agv[0]
    g = rgb_agv[1]
    b = rgb_agv[2]
    # the smallest color distance
    best_pix_dis = get_pixel_dist(pixels[0], r, g, b)
    # the pixel with the smallest color distance
    best_pix = pixels[0]
    for pix in pixels:
        pix_dist = get_pixel_dist(pix, r, g, b)
        # compare color_distance
        if pix_dist < best_pix_dis:
            best_pix_dis = pix_dist
            best_pix = pix
    return best_pix


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    # ----- YOUR CODE STARTS HERE ----- #
    for x in range(result.width):
        for y in range(result.height):
            # a list of the pixels, with the same coordinates.
            pixels = []
            for img in images:
                pixel = img.get_pixel(x, y)
                pixels.append(pixel)
            best_pix = get_best_pixel(pixels)
            # the result image
            result_pix = result.get_pixel(x, y)
            result_pix.red = best_pix.red
            result_pix.green = best_pix.green
            result_pix.blue = best_pix.blue
    # ----- YOUR CODE ENDS HERE ----- #
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
