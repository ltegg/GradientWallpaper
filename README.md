# GradientWallpaper

A Python 3.5 function to generate 2-colour gradient wallpapers. The function takes two colours (expressed as hexadecimal triplets), the screen resolution and the gradient direction (vertical or horizontal), and makes a .png of the gradient.

## Requirements

This script was written using Python 3.5, and needs `numpy` and `matplotlib`.

## Installation

Put `GradientWallpaper.py` in your wallpaper directory. 

## Usage

From a Python console, call

`GradientWallpaper(hex1, hex2, size, type, dir)`

Where

* `hex1` - A string of a hexadecimal triplet representing the first colour. Default is `hex1='ff0000'`.
* `hex2` - A string of a hexadecimal triplet representing the second colour. Default is `hex1='0000ff'`.
* `size` - The dimensions of the wallpaper, expressed as a two-element list. Default is `[1920,1080]`.
* `type` - Whether to generate a vertical (`'v'`) or a horizontal (`'h'`) gradient. Default is `'v'`.
* `dir`  - A path, relative to the present working directory, to save the images. Default is `''` (same as pwd).

An example script is included, to demonstrate usage.

## Screenshots

With `hex1=642b73, hex2=c64263, type='v'`:

![642b73+c64263](/examples/642b73+c64263.png?raw=true "642b73+c64263")

With `hex1=dce35b, hex2=45b649, type='h'`:

![dce35b+45b649](/examples/dce35b+45b649.png?raw=true "dce35b+45b649")
