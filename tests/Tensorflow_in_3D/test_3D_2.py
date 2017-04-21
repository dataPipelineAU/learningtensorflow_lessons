import numpy as np
def create_cube(bottom_lower=(0, 0, 0), side_length=5):
    """Creates a cube starting from the given bottom-lower point (lowest x, y, z values)"""
    bottom_lower = np.array(bottom_lower)
    points = np.vstack([
        bottom_lower,
        bottom_lower + [0, side_length, 0],
        bottom_lower + [side_length, side_length, 0],
        bottom_lower + [side_length, 0, 0],
        bottom_lower + [0, 0, side_length],
        bottom_lower + [0, side_length, side_length],
        bottom_lower + [side_length, side_length, side_length],
        bottom_lower + [side_length, 0, side_length],
        bottom_lower,
    ])
    return points
    
    
cube_1 = create_cube(side_length=2)
​
​
plot_basic_object(cube_1)

Figure 1
x=-1.24144 , y=8.76694 , z=-7.12935
