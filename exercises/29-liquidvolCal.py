# Please write a function that calculates liquid volume in a sphere using the following formula. The radius r  is always 10, so consider making it a default parameter.,
import math

def volume(h,r=10):
    p=math.pi
    a=4 * (p)*r**3
    b=(p)*h**2*(3*r-h)
    v= (a-b)/3
    return v
volume1=volume(2)
print(volume1)