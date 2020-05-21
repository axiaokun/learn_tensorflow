import tensorflow as tf

input1 = tf.placeholder(tf.float32)
# input1 = tf.placeholder(tf.float32, [2, 2])  # 可以规定结构,例如这里规定两行两列
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1, input2)  # 乘法运算

with tf.Session() as sess:
    print(sess.run(output, feed_dict={input1: [7.], input2: [2.]}))
