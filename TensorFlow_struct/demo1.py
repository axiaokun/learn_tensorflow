import tensorflow as tf
import numpy as np

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1+0.3


# create TensorFlow structure star
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases

loss = tf.reduce_mean(tf.square(y-y_data))
optinmizer = tf.train.GradientDescentOptimizer(0.5)  # 优化器
train = optinmizer.minimize(loss)  # 使用优化器减小误差


init = tf.initialize_all_variables()  # 初始化所有结构变量
# create TensorFlow structure end


sess = tf.Session()
sess.run(init)  # 激活

# 开始执行，每二十步打印一次
for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))


