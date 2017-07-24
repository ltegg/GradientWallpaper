def GradientWallpaper(hex1='ff0000',hex2='0000ff',size=[1920,1080],type='v',dir=''):
    """Makes nice gradients for your desktop
    
    Keyword arguments:
        hex1:   Hex code, without hash (#), as a string, for first colour
                default hex1='000000'
        hex2:   Hex code, without hash (#), as a string, for second colour
                default hex2='000000'
        size:   [width, height] of your screen, in pixels
                default size=[1920,1080]
        type:   Either a vertical ('v') or horizontal ('h') gradient
                default type='v'
        dir:    The directory to save into. Default is pwd.
                default dir=''
    
    """
    # %% Import libraries
    # Import numpy to handle arrays, and make a linspace
    import numpy as np
    # Import matplotlib to handle colourbars and images
    import matplotlib as mpl
    
    
    # %% Generate gradient
    # The resolution of the monitor, in pixels, as a numpy array
    size = np.array(size)

    # Catch the direction of the gradient
    if type == 'h':
        # An array with dimensions equal to the screen resolution, which 
        # increases in value HORIZONTALLY
        z = np.array([(1/size[0]) * np.linspace(0,size[0],num=size[0]),]
            *size[1])
    if type == 'v':
        # An array with dimensions equal to the screen resolution, which 
        # increases in value VERTICALLY
        z = np.transpose(np.array([(1/size[1]) * np.linspace(0,size[1],
            num=size[1]),]*size[0]))
    if not (type == 'h' or type == 'v'):
        import sys
        sys.exit("Unidentified type. Valid options are 'v' for vertical gradient, or 'h' for horizontal gradient")
        
    # RGB int tuples corresponding to the above strings
    rgb1 = tuple(int(hex1[i:i+2], 16) for i in (0, 2 ,4))
    rgb2 = tuple(int(hex2[i:i+2], 16) for i in (0, 2 ,4))
    
    # Make a dict specifing the start and end R, G and B values, from 0..1
    cdict = {'red':   [(0.0,   float(rgb1[0])/255,  float(rgb1[0])/255),
                       (1.0,   float(rgb2[0])/255,  float(rgb2[0])/255)],
             'green': [(0.0,   float(rgb1[1])/255,  float(rgb1[1])/255),
                       (1.0,   float(rgb2[1])/255,  float(rgb2[1])/255)],
             'blue':  [(0.0,   float(rgb1[2])/255,  float(rgb1[2])/255),
                       (1.0,   float(rgb2[2])/255,  float(rgb2[2])/255)]}
    
    # Construct a colourmap using the dictionary above
    cmap = mpl.colors.LinearSegmentedColormap('cmap',cdict,len(z[:,0]))
    
    
    # %% Make the image
    mpl.image.imsave((dir + hex1 + '+' + hex2 + '.png'),z,cmap = cmap)