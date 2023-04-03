# Image Helper Class

Write a Python class called `ImageHelper` that provides several static methods for working with images using the `cv2` and `numpy` libraries. The class should include the following methods:

- `read_color_image(path)`: Reads a color image from disk given its path.
- `read_gray_image(path)`: Reads a grayscale image from disk given its path.
- `read_image(path)`: Reads an image from disk unchanged given its path.
- `save_image(image, name, extension, path)`: Saves an image to disk given its name, extension, and path.
- `get_image_info(image)`: Returns all necessary information to describe an image.
- `show_image(image, title="Image")`: Displays an image in a window with the given title.
- `show_image_grid(images, rows, cols, title="Image Grid")`: Displays a grid of images in a window with the given title.
- `swap_red_blue(image)`: Swaps the red and blue channels of an image.

Make sure to include appropriate docstrings for each method and to handle any potential errors that may occur.
