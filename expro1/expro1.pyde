x=400.0
y=0.5
speed = 1.0
def setup():
    size(800,800);

def draw():
    rect(10,0,580,580);
    line(10,10,580,10);
    line(10,580,580,580);
    line(10,570,570,570);
    line(10,290,580,290);

    rect(mouseX,mouseY,60,30);
    move();
    display();
def move():
    global y;
    y=y+speed;
    if(y>580):
        y=0;
def display():
    fill(y,y/3,y/4);
    ellipse(x,y,50,60);
        
