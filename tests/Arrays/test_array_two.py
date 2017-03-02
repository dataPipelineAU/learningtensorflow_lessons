
def test_array_two():
    import matplotlib.image as mpimg
    import matplotlib.pyplot as plt
    import os
    # First, load the image
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = dir_path + "/MarshOrchid.jpg"
    image = mpimg.imread(filename)

    # Print out its shape
    print(image.shape)

    plt.imshow(image)
    #plt.show()

    print("two")
