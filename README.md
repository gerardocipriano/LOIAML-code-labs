# Image Preprocessor Class

Write a Python class called `Preprocessor` that provides several methods for preprocessing images using the `cv2`, `numpy`, and `os` libraries. The class should include the following methods:

- `__init__(self, input_path)`: Initializes a new instance of the `Preprocessor` class with the given input path.
- `check_path(self)`: Checks if the input path is a valid directory and contains valid image files.
- `set_change_lum(self, value)`: Sets whether to change the luminosity of the images.
- `set_rotation(self, value)`: Sets whether to rotate the images.
- `set_scaling(self, value)`: Sets whether to scale the images.
- `set_translation(self, value)`: Sets whether to translate the images.
- `run(self)`: Runs the preprocessing pipeline on all valid image files in the input path.

In addition to the `Preprocessor` class, write a function called `show_image_grid(images, grid_size=(2, 2), window_name='Image Grid')` that displays a grid of images in a window with the given title.

Make sure to include appropriate docstrings for each method and function and to handle any potential errors that may occur.