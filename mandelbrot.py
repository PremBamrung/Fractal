import numpy
from numba import jit
import matplotlib.pyplot as plt
import time
from tqdm import tqdm


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + " ms")
        return result
    return wrapper

@jit
#@jit(nopython=True, parallel=True)
def mandelbrot(Re,Im,max_iter):
    c=complex(Re,Im)
    z=0.0j
 
    for i in range(max_iter):
        z=z*z+c
        if(z.real*z.real+z.imag*z.imag)>=4:
            return i
    return max_iter

dim=2000 
columns=dim
rows=dim
iterration=1000
result=numpy.zeros([rows,columns])

@time_it
#@jit
def main():
        for row_index, Re in enumerate(tqdm(numpy.linspace(-2,1, num=rows))):
                for column_index, Im in enumerate(numpy.linspace(-1,1,num=columns)):
                        result[row_index,column_index]=mandelbrot(Re,Im,iterration)

print("Dimensions :",dim," * ",dim)
print("Itération : ",iterration)
main()

plt.figure(dpi=150)
plt.imshow(result.T, cmap='hot',interpolation='bilinear',extent=[-2,1,-1,1])
plt.xlabel("Re")
plt.ylabel("Im")
plt.title("Figure de Mandelbrot")
plt.show()
