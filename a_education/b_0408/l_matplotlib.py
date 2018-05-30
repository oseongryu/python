import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
np.random.seed(2000)
y=np.random.standard_normal(30)
# x=range(len(y))
# plt.plot(x,y)
# # plt.show()
#
# plt.plot(y.cumsum())
# plt.grid(True)
# plt.xlim(-1.23)
# plt.ylim(np.min(y.cumsum())-1, np.max(y.cumsum())+1)
# plt.show()

plt.figure(figsize=(7, 4))
plt.plot(y.cumsum(), 'b', lw=1.5)
plt.plot(y.cumsum(), 'ro')
plt.grid(True)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.title('Sample Plot')
plt.show()