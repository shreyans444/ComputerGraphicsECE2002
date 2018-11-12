def setup():
    size(500, 500,P3D);

def draw():
    fill(mouseX-50,mouseY-40,mouseY,100)
    lights();
    ellipse(mouseX,mouseY,mouseX+50,mouseY+50
