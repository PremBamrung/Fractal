# https://murillogroupmsu.com/julia-set-speed-comparison/

import time #timing
import numpy as np #arrays
from numba import jit, prange

x_dim = 1000
y_dim = 1000
x_min = -1.8
x_max = 1.8
y_min = -1.8j
y_max = 1.8j

z = np.zeros((y_dim,x_dim),dtype='complex128')
for l in range(y_dim):
    z[l] = np.linspace(x_min,x_max,x_dim) -np.linspace(y_min,y_max,y_dim)[l]  

def julia_raw_python(c,z):
    it = 0
    max_iter = 100
    while(it < max_iter):
        #These will be expensive!
        for y in range(y_dim):
            for x in range(x_dim):
                if abs(z[y][x]) < 10: #Runaway condition
                    z[y][x] = z[y][x]**2 + c #square and add c everywhere
        it += 1
    return z

  
start = time.perf_counter()
julia_raw_python(-.4+.6j,z) #arbitrary choice of c
end = time.perf_counter()
print(end-start)




def julia_numpy(c,z):
    it = 0
    max_iter = 100
    while(it < max_iter):
        z[np.absolute(z) < 10] = z[np.absolute(z) < 10]**2 + c #the logic in [] replaces our if statement. This line
        it += 1                                                #updates the whole matrix at once, no need for loops!
    return z
  
start = time.perf_counter()
julia_numpy(-.4+.6j,z) #arbitrary choice of c
end = time.perf_counter()
print(end-start)


@jit(nopython=True,parallel = True)
def julia_raw_python_numba(c,z):
    it = 0
    max_iter = 100
    while(it < max_iter):
        #These will be expensive!
        for y in prange(y_dim): #special loops for Numba! range -> prange
            for x in prange(x_dim):
                if abs(z[y][x]) < 10: #Runaway condition
                    z[y][x] = z[y][x]**2 + c #square and add c everywhere
        it += 1
    return z
  
start = time.perf_counter()
julia_raw_python_numba(-.4+.6j,z)
end = time.perf_counter()
print(end-start)