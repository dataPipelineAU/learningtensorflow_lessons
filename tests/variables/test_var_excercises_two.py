import tensorflow as tf


def test_var_thee():
    x = tf.Variable(0, name='x')

    model = tf.global_variables_initializer()

    with tf.Session() as session:
        for i in range(5):
            session.run(model)
            x = x + 1
            print(session.run(x))