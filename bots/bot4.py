poligon = [['.'] * 30 for i in range(30)]
x_b=0
y_b=0
poligon[y_b][x_b]="b"
bcolor="b"
pcolor="p"
#def fillColor(color):
def drawB(direction):
    global x_b,y_b
    global poligon
    if y_b+1<=29 and direction == "up" and (poligon[y_b+1][x_b]=='.' or poligon[y_b+1][x_b]==bcolor):
        poligon[y_b + 1][x_b]=bcolor
        y_b+=1
        return
    elif x_b-1>=0 and direction == "left" and (poligon[y_b][x_b-1]=='.' or poligon[y_b][x_b-1]==bcolor):
        poligon[y_b][x_b-1]=bcolor
        x_b-=1
        return
    elif x_b+1<=29 and direction == "right" and (poligon[y_b][x_b+1]=='.' or poligon[y_b][x_b+1]==bcolor):
        poligon[y_b][x_b+1]=bcolor
        x_b+=1
        return
    elif y_b-1>=0 and direction == "down" and (poligon[y_b-1][x_b]=='.' or poligon[y_b-1][x_b]==bcolor):
        poligon[y_b-1][x_b]=bcolor
        y_b-=1
        return
x_p=0
y_p=29
poligon[y_p][x_p]=pcolor
def drawP():
    global x_p,y_p
    global poligon
    while y_p-1>=0 and (poligon[y_p-1][x_p]=='.' or poligon[y_p-1][x_p]==pcolor):
        poligon[y_p-1][x_p]=pcolor
        y_p-=1
        direct="up"
        drawB(direct)
    while x_p+1<=29 and (poligon[y_p][x_p+1]=='.' or poligon[y_p][x_p+1]==pcolor):
        poligon[y_p][x_p+1]=pcolor
        x_p+=1
        direct = "right"
        drawB(direct)
    while y_p+1<=29 and (poligon[y_p+1][x_p]=='.' or poligon[y_p+1][x_p]==pcolor):
        poligon[y_p+1][x_p]=pcolor
        y_p+=1
        direct = "down"
        drawB(direct)
    while x_p-1>=0 and (poligon[y_p][x_p-1]=='.' or poligon[y_p][x_p-1]==pcolor):
        poligon[y_p][x_p-1]=pcolor
        x_p-=1
        direct = "left"
        drawB(direct)
    if (x_p==29 or (poligon[y_p][x_p+1]!='.' and poligon[y_p][x_p+1]!=pcolor)):
        if (x_p==0 or (poligon[y_p][x_p-1]!='.' and  poligon[y_p][x_p-1]!=pcolor)):
            if (y_p==29 or (poligon[y_p+1][x_p]!='.' and poligon[y_p+1][x_p]!=pcolor)):
                if(y_p==0 or (poligon[y_p-1][x_p]!='.' and poligon[y_p-1][x_p-1]!=pcolor)):
                    return
while (True):
    if ((x_p==29 or poligon[y_p][x_p+1]!='.') and (x_p==0 or poligon[y_p][x_p-1]!='.') and (y_p== 29 or poligon[y_p+1][x_p]!='.') and (y_p==0 or poligon[y_p-1][x_p]!='.')):
        break
    drawP()
print(*poligon, sep='\n')
