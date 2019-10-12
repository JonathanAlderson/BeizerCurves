import matplotlib.pyplot as plt
from matplotlib import animation
import time

def calcXLim(curve,padding=0.25):
    minX = min([p.x for p in curve.points])
    maxX = max([p.x for p in curve.points])
    return(minX - minX*padding,maxX + maxX * padding)

def calcYLim(curve,padding=0.25):
    minY = min([p.y for p in curve.points])
    maxY = max([p.y for p in curve.points])
    return(minY - minY*padding,maxY + maxY * padding)

def lerp(a,b,t):
    return Point(a.x + (b.x-a.x)*t,a.y + (b.y-a.y)*t)

class Point:
    x = 0
    y = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return ("(" + str(self.x) + "," + str(self.y) + ")")

class BCurve:
    points = []
    order = 0
    child = 0
    focalPoint = 0

    def __init__(self,points,t):
        self.points = points
        self.order = len(points)
        if(len(points) > 1):
            self.child = BCurve(self.calc(t),t)
        else:
            self.child = None

        self.focalPoint = self.getFocalPoint()

    def getFocalPoint(self):
        if(self.order == 1):
            return self.points[0]
        else:
            child = self.child
            return child.points[0]

    def calc(self,t):
        ret = []
        for i in range(len(self.points)-1):
            ret.append(lerp(self.points[i],self.points[i+1],t))
        return(ret)

    def getX(self):
        return([p.x for p in self.points])
    def getY(self):
        return([p.y for p in self.points])




colours = ['b','g','r','m','y','b','g','r','m','y']

startPoint = [Point(0,0),Point(10,10),Point(10,0),Point(0,10)]                                                              # the reverse
startPoint = [Point(0,0),Point(7,5),Point(5,8)]
startPoint = [Point(0,0), Point(3,10),Point(6,0),Point(9,10),Point(12,0),Point(15,10),Point(18,0),Point(21,10)]             # straight line
startPoint = [Point(0,0),Point(7,5),Point(5,8),Point(0,6.5),Point(2.5,3)]                                                   # basic example
startPoint = [Point(0,5),Point(0,10),Point(5,10),Point(10,10),Point(10,5),Point(10,0),Point(5,0),Point(0,0),Point(0,5)]     # circle
startPoint = [Point(0,0),Point(5,10),Point(10,0),Point(0,0),Point(5,10),Point(10,0),Point(0,0)]                             # triangle triangle





curve = BCurve(startPoint,0)


plt.ion()
plt.figure("Beizer Curve")
plt.xlim(calcXLim(curve))
plt.ylim(calcYLim(curve))
plt.title("Beizer Curve")
plt.xlabel('$x$')
plt.ylabel('$y$')

# while curve.order > 1:
#     plt.plot(curve.getX(),curve.getY(),colours[curve.order])
#     plt.plot(curve.focalPoint.x,curve.focalPoint.y, 'ro')
#     print(curve.focalPoint)
#     curve = curve.child

steps = 400
x = []
y = []
for i in range(steps):
    curve = BCurve(startPoint,i/steps)
    while curve.order > 1:
        plt.plot(curve.getX(),curve.getY(),colours[curve.order])
        curve = curve.child
    x.append(curve.focalPoint.x)
    y.append(curve.focalPoint.y)
    plt.plot(x,y,colours[curve.order]+"o")
    plt.draw()
    plt.pause(0.0001)
    plt.clf()

plt.show()
time.sleep(10)
