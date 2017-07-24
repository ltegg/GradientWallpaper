# Import the GradientWallpaper function
from GradientWallpaper import GradientWallpaper

# Specify your screen resolution as [width, height]
resolution = [1920, 1200]

# Specify a subfolder, relative to the pwd, to save the files into
subfolder = 'examples/'

# Make a single image, with a horizontal gradient
GradientWallpaper(hex1='dce35b',
                  hex2='45b649',
                  size=resolution,
                  type='h',
                  dir=subfolder)

# Make a list of colours to make images from
colourpairs = [
               ['ffc3a0', 'ffafbd'],
               ['642b73', 'c64263'],
               ['000000', '434343'],
              ]

# Loop through the pairs of colours, making vertical gradients, saving images 
# of each
for pair in colourpairs:
    GradientWallpaper(hex1=pair[0],
                      hex2=pair[1],
                      size=resolution,
                      dir=subfolder)
