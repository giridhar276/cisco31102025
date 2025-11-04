
#method1 - importing all the methods
import math
print(math.tan(1))
print(math.floor(23.3))

#method2 - importing with alias name 
import math as m 
print(m.log(2))
print(m.cos(2))

#method3 - importing required methods only
from math import floor,ceil,log 
print(floor(45.4))
print(ceil(34.3))
print(log(1))