# import random
# print(random.rand(1, 10))

# from random import *
# print(random())

from random import randint
fuel=randint(10,25)
print("car fuel tank holds "+str(fuel))
miles=randint(200,400)
print("the car can travel "+str(miles))
print("miles per gallon "+str(miles//fuel))
