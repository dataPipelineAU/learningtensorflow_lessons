import tensorflow as tf
import resource
import numpy as np


def test_interactive_two():

    session = tf.InteractiveSession()

    X = tf.constant(np.eye(10000))
    Y = tf.constant(np.random.randn(10000, 300))

    print("{} Kb".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))

    Z = tf.matmul(X, Y)

    Z.eval()

    print("{} Kb".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))

    session.close()