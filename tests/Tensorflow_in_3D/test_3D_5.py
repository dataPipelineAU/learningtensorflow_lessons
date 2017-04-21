def rotate_around_z(points, theta):
    theta = float(theta)
    rotation_matrix = tf.stack([[tf.cos(theta), tf.sin(theta), 0],
                                   [-tf.sin(theta), tf.cos(theta), 0],
                                   [0, 0, 1]])
    return tf.matmul(tf.to_float(points), tf.to_float(rotation_matrix))


with tf.Session() as session:
    result = session.run(rotate_around_z(cube_1, 75))


plot_basic_object(result)
