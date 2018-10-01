from Processing import *
window(500, 500)

def setup(): 
    size(100, 100, P3D)
    background(0)
    noStroke()
    
# Draw a simple earth
def drawEarth(x, y, s):
    pushMatrix()
    translate( x, y )
    scale( s )
    fill(128, 128, 255)
    ellipse(0, 0, 100, 100)
    popMatrix()
    
def draw(): 
    # Include lights() at the beginning
    # of draw() to keep them persistent 
    #lights()

    drawEarth( 100, 150, 0.3 )
    
# Set up looping
onLoop += draw
frameRate(100)
loop()
    