import tensorflow as tf


def test_placeholder_one():
    x = tf.placeholder("float", None)
    y = x * 2

    with tf.Session() as session:
        result = session.run(y, feed_dict={x: [1, 2, 3]})
        print(result)