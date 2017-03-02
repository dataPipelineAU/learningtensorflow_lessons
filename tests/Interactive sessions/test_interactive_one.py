import tensorflow as tf


def test_interactive_one():

    session = tf.InteractiveSession()

    x = tf.constant(list(range(10)))

    print(x.eval())

    session.close()