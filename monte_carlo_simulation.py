from scipy.stats import norm
import matplotlib.pyplot as plt
import random

class MonteCarloSim:
    
    #Constructs a Monte Carlo Simulation object with default values for base, height and number of Trials
    def __init__(self, myFun, base=[0,1], height=[0,1], nTrials=10000):
        self.myFun = myFun
        self.base = base
        self.height = height
        self.nTrials = nTrials

    #Gets the coordinates of the base interval
    def getX(self):
        return self.base
    
    #Changes the coordinates of the base interval
    def setX(self, base):
        self.base = base
        return self.base
    
    #Gets the coordinates of the height interval
    def getY(self):
        return self.height
    
    #Changes the coordinates of the height interval
    def setY(self, height):
        self.height = height
        return self.height
    
    #Gets the number of simulations
    def getN(self):
        return self.nTrials
    
    #Sets the number of simulations
    def setN(self, n):
        self.nTrials = n
        return self.nTrials
    
    #Creates a random number between two float variables a and b
    def rand(self, a, b):
        return random.uniform(a, b)
    
    #Returns the area under the curve of the initially given function (self.myFun(x))
    def getArea(self):
        area = 0
        for x in range(self.nTrials):
            x = self.rand(self.base[0], self.base[1])
            y = self.rand(self.height[0], self.height[1])
            if y <= self.myFun(x):
                area += 1
        return area/self.nTrials
      
    def testFun(self, x):
        return norm.pdf(x)

    def testArea(self, intervals):
        return norm.cdf(intervals[1]) - norm.cdf(intervals[0])  
    
    
def main():

    def myFun(value):
            return norm.pdf(value)
        
    MCS = MonteCarloSim(myFun) 
    inputForMonteCarloSim = int(input("Pleas insert a value that should be used for the standard normal distribution of the Monte Carlo Simulation: "))
    myFun(inputForMonteCarloSim)
    MCS.testFun(inputForMonteCarloSim) 
        
    MCS.setX([-5,5])
    MCS.setY([-10,5])
    MCS.setN(100000)
 
    x = MCS.getArea()
    print("This is getArea:", x)
    y = MCS.testArea([-10, 5]) 
    print("This is testArea:", y)
        

    results = [ ]
    x = 100
    numberOfTrials = [ ]
    randomMultipler = random.randint(2, 3)
        
    while x <= 10000:
        numberOfTrials.append(x)
        x*=randomMultipler
        
    print("Number of Trials: ", numberOfTrials)

    for x in numberOfTrials:
        MCS.setN(x)
        results.append(MCS.getArea())
        
    print("Results: ", results)

    
    deviation = [ ]
    for i in range(len(results)):
        values = results[i] - MCS.testArea([-5,5])
        deviation.append(values)
    print("Diviation:", deviation)
        

    plt.plot(numberOfTrials, deviation) 
    plt.title("Error Analysis")
    plt.ylabel("Deviation")
    plt.xlabel("Number of simulations")
        
main()