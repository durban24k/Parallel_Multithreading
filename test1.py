# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import multiprocessing as mp
np=mp.cpu_count()
print(np)


# %%
import numpy


# %%
print("Hello")


# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

start_time=time.time()
p=np.linspace(0,20,100)
plt.plot(p,np.sin(15*p))
plt.show()
end_time=time.time() - start_time
print(end_time)



# %%
