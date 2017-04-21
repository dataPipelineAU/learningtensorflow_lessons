import tensorflow as tf

# Point 1
x1 = tf.constant(2, dtype=tf.float32)
y1 = tf.constant(1, dtype=tf.float32)
point1 = tf.stack([x1, y1])

# Point 2
x2 = tf.constant(-1, dtype=tf.float32)
y2 = tf.constant(1, dtype=tf.float32)
point2 = tf.stack([x2, y2])

# Combine points into an array
X = tf.transpose(tf.stack([point1, point2]))

B = tf.constant([[9, 3]], dtype=tf.float32)

parameters = tf.matmul(B, tf.matrix_inverse(X))

with tf.Session() as session:
    A = session.run(parameters)
    b = A[0][1]
    a = A[0][0]
    print("Equation: y = {a}x + {b}".format(a=a, b=b))
