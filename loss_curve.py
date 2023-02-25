import numpy as np

# #
# test = np.load('train_acc.npy')
#
# print(test)
#
#
import matplotlib.pyplot as plt
x = list(range(0,50))
y = np.load('miou.npy')
plt.plot(x, y, 'b-')  #
plt.xlabel("epoch")
plt.ylabel("miou")
# plt.show()
plt.savefig('miou.png')
