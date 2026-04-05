'''
import sys
sys.path.append('D:/Python/my_modules')
'''
# OR 
'''
on machine level we can do the path assigning by using the
environment variable setting by creating PYTHONPATH in 
the environment and in its value add the path of the modules
'''

print("name" , __name__)

# import module_1
# module_1.f1(1,2)
# module_1.f2()

# import module_1 as m1
# m1.f1(4,5)
# m1.f2()


# from module_1 import *
from module_1 import f1,f2
f1(4,5)
f2()


import module_2 as m2
m2.f11()
m2.f12()


import drawings.colors.color_1 as cl1

cl1.c1()
cl1.c2()

import drawings.graphics.TDImage.image_1 as ig
ig.img1()
ig.img2()