import tensorflow as tf

state = tf.Variable(0, name='counter')  # Variable设置变量
# print(state.name)
one = tf.constant(1)  # constant设置常量

new_value = tf.add(state, one)  # 给变量加上一次常量
update = tf.assign(state, new_value)  # 更新变量
init = tf.initialize_all_variables()  # must have if define variable

with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))
