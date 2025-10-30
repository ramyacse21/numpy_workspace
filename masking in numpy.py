###broadcasting
import numpy as np
a=np.array([3,5,np.nan,2,np.inf])
sum=np.sum(a)                              #nan
# print(sum)

b=np.ma.array(a,mask=[0,0,1,0,1],hard_mask=True)
c=np.ma.array(a,mask=[0,0,1,0,1],hard_mask=False)
mask=np.sum(b)
print(b)                    #[3.0 5.0 -- 2.0 --]

mas=b[~b.mask]
print(mas)         #[3.0 5.0 2.0]

b[2]=5
c[2] = 5
mask
mask=a[2]
print(mask)      #5.0
print(b)         #[3.0 5.0 -- 2.0 --]
print(c)         #[3.0 5.0 5.0 2.0 --]

b[1]=np.ma.masked_
masked=b[1]
print(masked)
print(b)

                                          