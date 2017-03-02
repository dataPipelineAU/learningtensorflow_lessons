import tensorflow as tf


def test_linear_two():
    points = tf.constant([[2, 1],
                     [0, 5],
                     [-1, 2]], dtype=tf.float64)

    A = tf.constant([
        [2, 1, 1],
        [0, 5, 1],
        [-1, 2, 1]
    ], dtype=tf.float64)

    B = -tf.constant([[10], [30], [10]], dtype=tf.float64)

    X = tf.matrix_solve(A, B)

    with tf.Session() as session:
        result = session.run(X)
        D, E, F = result.flatten()
        # result should be Equation: x**2 + y**2 + -2.0x + -6.0y + 0.0 = 0

        print("Equation: x**2 + y**2 + {D}x + {E}y + {F} = 0".format(**locals()))
