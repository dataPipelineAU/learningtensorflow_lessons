import tensorflow as tf


def test_var_five():
    x = tf.constant(35, name='x')
    y = tf.Variable(x + 5, name='y')

    model = tf.global_variables_initializer()

    with tf.Session() as session:
        session.run(model)
        print(session.run(y))

    import numpy as np
    data = np.random.randint(1000, size=10000)