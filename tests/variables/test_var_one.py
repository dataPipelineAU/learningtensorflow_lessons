import tensorflow as tf


def test_var_four():
    x = tf.constant(35, name='x')
    y = tf.Variable(x + 5, name='y')

    print(y)
