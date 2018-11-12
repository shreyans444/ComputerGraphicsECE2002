def setup():
    size(500, 500,P3D);

def draw():
    
    background(255);
    fill(mouseX,mouseY,mouseY,100)
    translate(mouseX+100,mouseY+100);
    lights();
    sphere(250);
