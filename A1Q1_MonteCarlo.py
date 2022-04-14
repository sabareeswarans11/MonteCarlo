"""
coding -UTF-8
To Calculate Overlapped Region between Two given Circle Using MonteCarlo Approach
Author: Sabareeswaran Shanmugam
Generic Approach (This program works for different Values of circle equations c1 ,c2)

"""
import math
import numpy as np

class Overlapped_area_circle:
    def __init__(self):
        self._c1 = [0]
        self._c2 = [0]
        self._N =None

    # function to get the equation of circle (c1),(c2) and N(number of Random points)
    def get_c1(self):
        return self._c1

    def get_c2(self):
        return self._c2

    def get_N(self):
        return self.N

    # function to set the equation of circle (c1),(c2) and N(number of Random points)

    def set_c1(self, a):
        self._c1 = a

    def set_c2(self, b):
        self._c2 = b

    def set_N(self, c):
        self._N = c

    def assign(self,_c1,_c2,_N):
        #circle c1
        x1 = self._c1[0]
        y1 = self._c1[1]
        r1 = self._c1[2]
        #circle c2
        x2 = self._c2[0]
        y2 = self._c2[1]
        r2 = self._c2[2]

        Random_points= self._N
        print('Number of Random Pts Generated by random.rand (N):',Random_points)

        if math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)) >= (r1 +r2):
            #no intersection (Area of overlapped region is zero)
            Area=0
        else:
            a_min = x1 - r1 - 2 * r2
            a_max = x1 + r1 + 2 * r2
            b_min = y1 - r1 - 2 * r2
            b_max = y1 + r1 + 2 * r2
            print("X-coordinates(x1,y1):",a_min,a_max)
            print("Y-coordinates(X2,y2):",b_min,b_max)
            #Monte Carlo algorithm
            count = 0
            for x in range(Random_points):
                rand_x = (a_max -a_min)*np.random.rand() +a_min
                rand_y = (b_max -b_min)*np.random.rand() +b_min
                if (math.sqrt((rand_x - x1)**2 + (rand_y - y1)**2) < r1) and (math.sqrt((rand_x - x2)**2 + (rand_y - y2)**2) < r2):
                    count = count + 1
            Area = ((a_max - a_min) * (b_max - b_min))* count / Random_points

        print('Area Of Overlapped region between two circle using MonteCarlo Approach(Approximate value):',Area)

if __name__ == '__main__':
    MonteCarlo = Overlapped_area_circle()
    #generic function
    #circle1[center c1, center c2, radius r1]
    #circle2[center c1, center c2, radius r2]
    MonteCarlo.assign(MonteCarlo.set_c1([0, 0, 2]), MonteCarlo.set_c2([2, 2, 2]), MonteCarlo.set_N(100000))
"""
Reference
https://stackoverflow.com/questions/35682835/find-area-of-two-overlapping-circles-using-monte-carlo-method
https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html?highlight=numpy%20random%20rand

"""
