import math
class Map(object):
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color=color
    def poli(self):
        arr=[[self.color] * self.x for i in range(self.y)]
        return arr
    def getCoord(self):
        return self.x,self.y
    def getColor(self):
        return self.color
mp=Map(30,30,'.').poli()
global x_m,y_m
x_m,y_m=Map(30,30,'.').getCoord()
class obj(object):
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color = color
    def getCoord(self):
        return self.x,self.y
    def getColor(self):
        return self.color
global x_b,y_b
x_b,y_b=obj(10,14,'b').getCoord()
color_b='b'
global x_p,y_p
x_p,y_p=obj(29,29,'p').getCoord()

def inRad(dx,dy,rad):
    if pow((x_p-x_b),2)+pow((y_p-y_b),2)==pow(rad,2):
        return True
def findCrossingGl():
    k=y_m/x_m
    kb=-1/k
    x = y_b - kb*x_b / k - kb
    y = k*x
    return x,y
def findCrossingPob():
    k=1/(x_m-1)
    kb=-1/k
    x = y_b - kb*x_b / k - kb
    y = k*x
    return x,y
def mvLeft():
    global x_b
    x_b -= 1
    return mp
def mvUp():
    global y_b
    y_b -= 1
    return mp
def mvDown():
    global y_b
    y_b += 1
    return mp
def mvRight():
    global x_b
    x_b += 1
    return mp
def drawColor(x,y,color):
    mp[y][x]=color
    return mp
x_cg,y_cg=findCrossingGl()
x_cp,y_cp=findCrossingPob()
lgthGl=math.sqrt(pow(x_cg-x_b,2)+pow(y_cg-y_b,2))
lgthPob=math.sqrt(pow(x_cp-x_b,2)+pow(y_cp-y_b,2))
if (lgthGl>=lgthPob):
    if y_b<y_cp:
        while y_b!=y_cp:
            mvDown()
            mvRight()
            if y_b != y_cg:
                drawColor(x_b, y_b, color_b)
    elif y_b > y_cp:
        while y_b != y_cp:
            mvUp()
            mvLeft()
            if y_b != y_cg:
                drawColor(x_b, y_b, color_b)
elif (lgthGl<lgthPob):
    if y_b < y_cg:
        while y_b != y_cg:
            mvDown()
            mvLeft()
            if y_b != y_cg:
                drawColor(x_b,y_b,color_b)
    elif y_b > y_cg:
        while y_b != y_cg:
            mvUp()
            mvRight()
            if y_b!=y_cg:
                drawColor(x_b, y_b, color_b)
print(*mp, sep='\n')
