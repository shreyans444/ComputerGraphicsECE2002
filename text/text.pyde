def setup():
    size(1000,1000);
    background(0);

def draw():
    fill(60, 30);
    rect(0, 0, width, height);

def keyPressed():
    fill('#ff0000');
    textSize(random(100,400));
    text(key, random(300), random(100,400));
