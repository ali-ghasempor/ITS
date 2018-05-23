import random
import matplotlib.pyplot as plt
import re

class Car:
    number = 0
    df = []
    med = 0
    def __init__(self):
        self.speed = 0.1
        # self.acc = random.randint(-10,10)
        self.time = 0
        Car.number += 1
        self.data = []
        Car.df = []
        self.x0 = random.randint(0,100)
        self.x = 0
        self.med = Car.med

    def run(self,acc1):
        while True:
            # x = self.speed + self.acc*self.time
            self.x = 0.5*acc1*self.time**2 + self.speed*self.time + self.x0
            self.time += 1
            if (self.time > 10):
                break
            self.data.append(self.x)
           # print(self.number , x)
        print(self.number, self.data)
        return (self.data)

    def get_number(self):
        return self.number

    def plot(self):
        # plt.plot(self.data)
        plt.plot(self.data)
        plt.grid(True)
        plt.ylabel('distance')
        plt.xlabel('time')
        #plt.show()

    def full_data(self):
        for i in range(len(self.data)):
            Car.df.append(self.data[i])
        # print("full data " ,Car.df)
    def median(self):
        self.med += self.data.pop()
        return self.med-self.x0

data = ""
number_of_car = 10
for i in range(number_of_car):
    i = Car()
    count = random.randint(-10, 10)
    if( int(i.get_number()) >= number_of_car*(3/4) ):
        count=abs(count)
    elif ( int(i.get_number()) >= 0.5*number_of_car ):
            count = -0.1* count
    i.run(count)
    i.plot()

# file = open("data.txt","a")
i.full_data()
i.median()
# file.write(str(i.median()/i.get_number()) + "\n")
print(data.strip('['))
i.get_number()
plt.show()
# data = re.sub(']','',data).strip()
# data = re.sub('\[','',data).strip()
# print(data)
# file.close()
