base=40
x=250
y=250
i=250
j=0
l=250
m=460
changex=-1
changey=-5

def setup():
    size(500,500)
    x=random(width)
    y=height-base
def draw():
    background(0)
    global x
    global y
    global l
    global m
    global changex
    global changey
    rect(i,j,100,base)
    rect(l,m,100,base)
    ellipse(x,y,10,10)
    x=x+changex
    y=y+changey
    if(x<0 or x>width):
        changex=-changex
    if(y<0):
        changey=-changey
    if(y>height-base):
        if(x<i and x<j+200):
            changey=-changey
        if(x>l and x<m+200):
            changey=-changey
        

            
            
    if(y>height):
        
         exit
def keyReleased():
    global i;
    global j;
    global l;
    global m;

    if(key==CODED):
        
    
        if(keyCode==LEFT):

            i=i-30;
        elif(keyCode==RIGHT):
            i=i+30;
def keyPressed():
    global l;
    

        
        
    if(key=='a' or key=='A' ):
            l=l-30;
    elif(key=='d' or key=='D'):
            l=l+30;

             
                
            
             
        
            
        
           
