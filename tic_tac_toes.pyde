def setup():
    size(500,500)

board =  [0,0,0,0,0,0,0,0,0]
turn = "x"
def draw():
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
