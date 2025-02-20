def setup():
    size(400,900)
    background(128,128,128)
    

rect_color = 255
decrement = 0
y_axis = 0
y_axis_anim = 0

def draw():
    global decrement
    global rect_color
    global y_axis_anim
#     
#
    y_axis_anim = y_axis_anim + 1
    decrement = decrement + 1
    background(128,128,128)
    
    fill(0, rect_color - decrement%255, 0)
    rect(0,y_axis + y_axis_anim%900, 900, 400)
    
    
    
    
    