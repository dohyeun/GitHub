# jupyter notebook magic command '%%writefile' for editing a filter
%%writefile test.py

import matplotlib.pyplot as plt
import numpy as np

def plot():
  X=np.random.randn (50)
  Y = 2*X+np.random.randn(50)

  plt.plot(X,Y,'ro', label='Data')
  plt.grid()
  plt.legend()
  plt.show()