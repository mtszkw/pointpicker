![Flake8](https://github.com/mtszkw/image-annotation/workflows/Flake8/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Image Annotation

Annotate **points** or **bounding boxes** in images using simple GUI (running on top of *matplotlib*).

## Installation

Run `pip install requirements.txt` in your local environment.

## Running

Run `python annotate.py` to without any arguments or with `-h` to display help (using `docopt`). The only required argument is the absolute path to the directory with images. At the moment there's no way to filter images by name or extension - all images within the directory will be read and displayed.

To run the application using sample data (point selection, no annotations limit, no window timeout):

```
python annotate.py ./data/
```

## Usage

After you run the application, a window with your first image should pop-up. Use:

* *Left mouse-button* to select a point in image,
* *Right mouse-button* to undo selection (can be used multiple times),
* *Middle mouse-button* to accept existing selections and save them to file.
