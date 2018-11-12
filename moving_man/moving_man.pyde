def setup():
    size(500, 500);
    
def draw():
    background(255)
    translate(mouseX-70,mouseY-70)
    fill(mouseX,mouseY,mouseY,100)
    ellipse(250,50,100,100);
    noFill();
    rect(250,101,1,200);
    print(mouseX,mouseY);
    line(250,173,350,243);
    line(250,173,150,243);
    line(250,301,190,425);
    line(250,301,310,425);
    
    
