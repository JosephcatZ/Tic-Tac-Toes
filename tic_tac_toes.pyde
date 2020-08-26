def setup():
    size(500,500)

board =  [0,0,0,0,0,0,0,0,0]
#0-horizontal 1-vertical 2- diagonal
wincons = [
           [0,1,2,0],
           [3,4,5,0],
           [6,7,8,0],
           [0,3,6,1],
           [1,4,7,1],
           [2,5,8,1],
           [0,4,8,2],
           [6,4,2,3]
           ]

turn = "x"
def draw():
    if Win==False:
        dBoard()
def dBoard():
    chalk = loadImage("Blackboard.jpg")
    image(chalk,0,0,500,500)
    textFont(loadFont("ChalkboardSE-Light-48.vlw"),48)
    global board
    noFill()
    strokeWeight(4)
    stroke(255)
    line(100,200,400,200)
    line(100,300,400,300)
    line(200,100,200,400)
    line(300,100,300,400)
    drawchar(0,150,150)
    drawchar(1,250,150)
    drawchar(2,350,150)
    drawchar(3,150,250)
    drawchar(4,250,250)
    drawchar(5,350,250)
    drawchar(6,150,350)
    drawchar(7,250,350)
    drawchar(8,350,350)
    noFill()
    if(turn == 'x'):
        stroke(0,0,255)
        line(90,490,10,410)
        line(10,490,90,410)
    else:
        stroke(255,0,0)
        ellipse(450,450,80,80)
    fill(255)
    textSize(50)
    textAlign(CENTER,CENTER)
    text("Turn",250,450)
Win = False
def checkWin():
    global Win
    Wins=[]
    for i in wincons:
        if equal(i[0],i[1],i[2]):
            dBoard()
            if board[i[0]] == 'x':
                stroke(0,0,255)
            else:
                stroke(255,0,0)
            Wins.append(i)
    for i in Wins:
        if i[3] == 0:
            line(getx(i[0],-50),gety(i[0],0),getx(i[2],50),gety(i[2],0))
        elif i[3] == 1:
            line(getx(i[0],0),gety(i[0],-50),getx(i[2],0),gety(i[2],50))
        elif i[3] == 2:
            line(getx(i[0],-50),gety(i[0],-50),getx(i[2],50),gety(i[2],50))
        if i[3] == 3:
            line(getx(i[0],-50),gety(i[0],50),getx(i[2],50),gety(i[2],-50))
        Win = True
def equal(a,b,c):
    if(board[a]==board[b] and board[b]==board[c] and board[c] != 0):
        return(True)
    else:
        return(False)
def getx(n,xo):
    return(150+xo+(n%3)*100)
def gety(n,yo):
    return(150+yo+(n-n%3)*100/3)
def drawchar(bp,x,y):
    noFill()
    if (board[bp] == 'o'):
        stroke(255,0,0)
        ellipse(x,y,80,80)
    elif(board[bp] == 'x'):
        stroke(0,0,255)
        line(x+40,y+40, x-40,y-40)
        line(x-40,y+40,x+40,y-40)
    elif(x-50< mouseX and mouseX < x+50 and y-50<mouseY and mouseY<y+50):
        noStroke()
        fill(255,255,0)
        rect(x-40,y-40,80,80)
        
def mouseClicked():
    global turn, board
    if(board[int(mouseX-100)/100 + 3*int(int(mouseY-100)/100)]==0):
        board[int(mouseX-100)/100 + 3*int(int(mouseY-100)/100)]=turn
        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'
    checkWin()
