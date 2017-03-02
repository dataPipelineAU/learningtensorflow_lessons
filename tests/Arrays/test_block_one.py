import os

import matplotlib.image as mpimg

# First, load the image
dir_path = os.path.dirname(os.path.realpath(__file__))
filename = dir_path + "/MarshOrchid.jpg"
image = mpimg.imread(filename)

# Print out its shape
print(image.shape)