# Create a Python script to generate a synthetic dataset

Create a Python script named `synthetic_builder.py` that generates a synthetic dataset. The script should contain a dedicated class called `SyntheticBuilder` to perform this task.

During its initialization, the class will receive the path to a configuration file `config.json` as input. The file, in `json` format, will contain all the information necessary to generate the synthetic data.

During initialization, the class will read the `json` file, going through all the necessary sections and setting its own necessary member variables. Reading a `json` file is possible through the `json` package.

Three groups of synthetic data should be created, divided into training, test and validation categories. The three categories will effectively be three subfolders within the output folder.

With a dedicated `build` method, the synthetic generator must:
- Execute a for loop for x times, where x is the number of training objects to create.
- Execute a for loop for y times, where y is the number of testing objects to create.
- Execute a for loop for z times, where z is the number of validation objects to create.

At each step of the loops, you must:
- Create the synthetic image by launching the `create_synthetic_object` method.
- Apply preprocessing to the created image by launching the `apply_preprocessing` method.

The created images must be saved on disk within their respective folders: training, test and validation. Or saved within three separate files in `.npz` format:
- train.npz
- test.npz
- validation.npz

`.npz` is a file format provided by numpy that allows you to collect a collection of multidimensional arrays in a single entity.

In conclusion, create a synthetic dataset using the `SyntheticBuilder` class. Create 100 synthetic images divided into:
- 60 training images
- 20 test images
- 20 validation images