################ *for ##############
list1=["RBR","SS","YM"]
for x in list1:
    print(x)
############### *Range ################
n=90
for i in range(1,n,3):
    print(i)


############### *patten ##############
n=5
for i in range(0,n):
    print(i*"*")

############## *args##################
def Cars(*cars):
    print(cars)
    print(cars[1])
    print(cars[2])
    print(cars[:2])
Cars("Tata indica","OOOO","BMW")

################# *kwargs #######################

def Cars_and_Owners(**cars):
    print(cars["Tataindica"],cars["OOOO"],cars["Benz"])

Cars_and_Owners(Tataindica ="Rohanth",OOOO="Sowmiya",Benz="Yuva")

##################### _iter_ ##################

class Cars2:
    cars=[]
    def __init__(self,cars):
        self.cars=cars
    
    def __iter__(self):
        return iter(self.cars)

c1 = Cars2(["Tata indica","OOOO","BMW"])
for x in c1:
    print(x)

###########__next__############ 

a = ['a', 'e', 'i', 'o', 'u']

iter_a = iter(a)

print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))###copy###

############# built-in imports #########

from math import sqrt, pi

print(sqrt(400))

################split & Strip ##############
rbr = " kdjf sldkfbv dkbl kibvl adibdb "
print(list(rbr.strip(" ")))
print(list(rbr.split(" ")))
print(list(rbr.strip().split(" ")))


############# custum imports #########
from cus_module import rohanth
rohanth("hi")



