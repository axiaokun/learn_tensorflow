# 初步了解，结构定义

在TensorFlow的世界里，变量的定义和初始化是分开的，所有关于图变量的赋值和计算都要通过tf.Session的run来进行。

* tf.Variable

  tf.Variable(initializer,name),参数initializer是初始化参数，name是可自定义的变量名称
  
 