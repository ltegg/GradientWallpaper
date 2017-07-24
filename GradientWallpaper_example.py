# Import the GradientWallpaper function
from GradientWallpaper import GradientWallpaper

# Make a list of colours to make images from
colourpairs = [
               ['ff0000', '0000ff'],
               ['ff0000', '00ff00'],
               ['00ff00', '0000ff'],
               ['00ff00', 'ff0000'],
               ['0000ff', 'ff0000'],
               ['0000ff', '00ff00'],
              ]

# Specify your screen resolution as [width, height]
resolution = [1920, 1200]

# Loop through the pairs of colours, saving images of each
for pair in colourpairs:
    GradientWallpaper(hex1=pair[0],hex2=pair[1],size=resolution)
