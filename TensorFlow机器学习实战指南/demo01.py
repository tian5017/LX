# 激励函数
import tensorflow as tf

sess = tf.Session()

# Relu
print(sess.run(tf.nn.relu([-3., 3., 10.])))

# Relu6
print(sess.run(tf.nn.relu6([-3., 3., 10.])))

# sigmoid
print(sess.run(tf.nn.sigmoid([-3., 3., 10.])))

# tanh
print(sess.run(tf.nn.tanh([-3., 3., 10.])))

#
