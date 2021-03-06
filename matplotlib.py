

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

import matplotlib.pyplotot as plt

plt.plot([1, 2, 3, 4], "ro")
plt.show()

import numpy as np
x = np.arange(0,10, 0.1)
figl, fl_axes = plt.subplots(ncols=2, nrows=2, figsize=(15,10))
figl.suptitle("Minha primeira figura", size=30)

fl_axes[0, 0].plot(np.sin(x), label="sen(x)", color="red")
fl_axes[0, 0].plot(np.cos(x), label="cos(x)", color="black")
fl_axes[0, 0].set_title("Caixa 1")
fl_axes[0, 0].set_xlabel("Caixa 1 - label X")
fl_axes[0, 0].set_ylabel("Caixa 1 - label Y")
fl_axes[0, 0].legend()

fl_axes[0, 0].plot(np.cos(x))
fl_axes[0, 0].set_title("Caixa 2")

fl_axes[1, 0].plot(np.tan(x))
fl_axes[1, 0].set_title("Caixa 3")

fl_axes[1, 1].set_title("Caixa 4")
