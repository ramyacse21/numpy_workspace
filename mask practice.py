import numpy as np
arr = np.array([10, 20, 30, 40, 50])
mask = arr > 30
print(mask)         # [False False False  True  True]
print(arr[mask])    # [40 50]

mask = arr < 30
print(mask)           #[ True  True False False False]
print(arr[mask])      #[10 20]

     
arr = np.array([3, 7, 0, 10, 0])
idx = np.where(arr == 0)
print(idx)        #(array([2, 4]),)


