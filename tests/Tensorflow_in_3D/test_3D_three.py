import tensorflow as tf

def translate(points, amount):
    return tf.add(points, amount)


points = tf.constant(cube_1, dtype=tf.float32)
​
# Update the values here to move the cube around.
translation_amount = tf.constant([3, -3, 0], dtype=tf.float32)


translate_op = translate(points, translation_amount)
​
with tf.Session() as session:
    translated_cube = session.run(translate_op)


plot_basic_object(translated_cube)

Figure 2
x=4.26205 , y=1.58246 , z=-4.34219
