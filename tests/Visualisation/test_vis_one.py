import tensorflow as tf

def test_vis_two():
    a = tf.add(1, 2, )
    b = tf.multiply(a, 3)
    c = tf.add(4, 5, )
    d = tf.multiply(c, 6, )
    e = tf.multiply(4, 5, )
    f = tf.div(c, 6, )
    g = tf.add(b, d)
    h = tf.multiply(g, f)

    with tf.Session() as sess:
        print(sess.run(h))

    with tf.Session() as sess:
        writer = tf.summary.FileWriter("output", sess.graph)
        print(sess.run(h))
        writer.close()


    a = tf.add(1, 2, name="Add_these_numbers")
    b = tf.multiply(a, 3)
    c = tf.add(4, 5, name="And_These_ones")
    d = tf.multiply(c, 6, name="Multiply_these_numbers")
    e = tf.multiply(4, 5, name="B_add")
    f = tf.div(c, 6, name="B_mul")
    g = tf.add(b, d)
    h = tf.multiply(g, f)