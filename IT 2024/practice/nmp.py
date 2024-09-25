from numpy import random
from math import log
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# sns.displot([0, 1, 2, 3, 4, 5])

# plt.show()

# x = random.normal(loc=1, scale=2, size=(2, 3))

# print(x)

# sns.displot(random.normal(size=1000), kind="kde", )
# sns.displot(random.binomial(n=5, p=0.5, size= 20), kind="kde")
# sns.displot(random.poisson(lam=10, size=20), kind="kde")
# plt.show()





# arr = np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))
# print(np.__version__)

# x = random.randint(100)
# print(x)

# arr = np.array([1,2,3,4,5])
# random.shuffle(arr)
# print(arr)


# print(random.permutation(arr))


x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)

#
def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

#
if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')

#log at any base
nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15))