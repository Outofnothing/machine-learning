# coding: utf-8
import numpy as np
import time
from load_data import get_data


s = 0.000000000001
train, train_label, test, test_label = get_data()
np.random.seed(1)
w = np.random.random((3, 1))
b = 0.0
irate = 0.3  # 这是learning rate的初始值
decay_rate = 0.99989
start = time.clock()
for i in range(1, 30000):  # 在使用了learning rate decay 之后，学习速率变大了约8倍
    # forward propagation
    z = np.dot(w.T, train) + b
    a = 1 / (1 + np.exp(-z))
    # 加上一个很小的s， 避免因精度问题导致的log函数参数为0
    loss = -np.dot(train_label, np.log(a + s).T) - np.dot(1-train_label, np.log(1-a + s).T)
    print(loss)
    # back propagation
    dz = a - train_label
    db = np.sum(dz) / 524
    dw = np.dot(train, dz.T) / 524
    rate = irate*(np.power(decay_rate, i))
    w = w - rate*dw
    b = b - rate*db
print(w, b)
z_test = np.dot(w.T, test) + b
a_test = 1 / (1 + np.exp(-z_test))  # issue: 会产生warning： overflow in exp, 之前的也有
                                   # 解决方法包括安装bigfloat库， 可是没有成功安装
a_test[a_test >= 0.5] = 1
a_test[a_test < 0.5] = 0
accuracy = 1 - np.sum(np.fabs(a_test - test_label)) / 175  # 与标准label相减后求绝对值就是错误预测的数量
print("Accuracy: %s" % accuracy)
end = time.clock()
print("time: " + str(end - start))
