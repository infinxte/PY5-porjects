def setup():
    size(600,400)
    smooth()
    no_stroke()
    
    
#backgrund changes from black and its transperacy increases untill it reaches yellow
# i want my final color to be (RED: 225, GREEN: 166, BLUE: 0)

#so my green and blue variables for should start at 0 and accumulare utill that number is reached

red_rgb = 0
green_rgb = 0
blue_rgb = 0
sun_rise = 600




def draw():
    global red_rgb
    global green_rgb
    global blue_rgb
    global sun_rise
    
    #background
    background((red_rgb), (green_rgb), blue_rgb )
    
    
    #sun
    fill(255,135,5,60)
    circle(300, (sun_rise),180)
    fill(255,100,0,100)
    circle(300, (sun_rise), 140)
    
    if sun_rise > 148:
        sun_rise = sun_rise - 2
        
    
    #mountains
    fill(110,50,18)
    triangle(200,400,520,253,800,400)
    fill(110,95,20)
    triangle(200,400,520,253,350,400)
    
    fill(150,75,0)
    triangle(-100, 400, 150,200, 400,400)
    fill(100,50,12)
    triangle(-100,400, 150,200,0,400)
    
    fill(150,100,0)
    triangle(200,400,450,250,800,400)
    fill(120,80,50)
    triangle(200,400,450,250,300,400)
    
    
    if red_rgb < 255:
        red_rgb = red_rgb + 1
    
    if green_rgb < 166:
        green_rgb = green_rgb + 1
    
    
    