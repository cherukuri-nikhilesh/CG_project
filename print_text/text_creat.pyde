def setup():
    size(600,600);
    background(0);

def draw():
   background(0);
   fill(200,10,10,200);
   ellipse(300,300,width,height);
   if (keyPressed==True):
       fill(255);
       textSize(random(20,200));
       text(key,random(30,300),random(30,300));
       
# def keyPressed():
#     textSize(random(20,200));
#     text(key,random(width),random(height));
