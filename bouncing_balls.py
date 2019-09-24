from visual import *
from math import *
import random
import itertools

scene.caption = """Right button drag or Ctrl-drag to rotate "camera" to view scene.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
     On a two-button mouse, middle is left + right.
Shift-drag to pan left/right and up/down.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

side = 4.0
thk = 0.3
s2 = 2*side - thk
s3 = 2*side + thk

n_ball = 50
ball_size = 0.3
balls = []
ball_pos = []
ball_p = []
ball_mass = 1

wallR = box (pos=vector( side, 0, 0), size=vector(thk, s2, s3),  color = color.gray(0.7))
wallL = box (pos=vector(-side, 0, 0), size=vector(thk, s2, s3),  color = color.gray(0.7))
wallB = box (pos=vector(0, -side, 0), size=vector(s3, thk, s3),  color = color.gray(0.7))
wallT = box (pos=vector(0,  side, 0), size=vector(s3, thk, s3),  color = color.gray(0.7))
wallBK = box(pos=vector(0, 0, -side), size=vector(s2, s2, thk), color = color.gray(0.7))


#create balls
for i in range(n_ball):
    x = 1*random.randint(-3, 3)-1/2
    y = 1*random.randint(-3, 3)-1/2
    z = 1*random.randint(-3, 3)-1/2
    colorRandom = (random.uniform(0, 1),random.uniform(0, 1),random.uniform(0, 1))
    each_ball_mass = round(random.uniform(0, 0.3), 2)
    if i == 0:
        balls.append(sphere(pos=vector(x,y,z), radius = each_ball_mass, color=color.yellow, make_trail=True)) 
    else: balls.append(sphere(pos=vector(x,y,z), radius = each_ball_mass, color=color.hsv_to_rgb(colorRandom)))
    ball_pos.append(vector(x,y,z))
    ball_p.append(vector(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))) 

#ball = sphere (color = color.hsv_to_rgb(colorRandom), radius = 0.4, make_trail=False, retain=200)
#ball.mass = 1.0
#ball.p = vector (-random.uniform(0, 1), -random.uniform(0, 1), +random.uniform(0, 1))

side = side - thk*0.5 - ball_size


dt = 0.3
while True:
    rate(10)

    colorRandom1 = (random.uniform(0, 1),random.uniform(0, 1),random.uniform(0, 1))
    
    #update position
    for i in range(n_ball):
        balls[i].pos = ball_pos[i] = ball_pos[i] + (ball_p[i]/ball_mass)*dt



    for j in range(n_ball):
        if not (side > ball_pos[j].x > -side):
            ball_p[j].x = -ball_p[j].x
        if not (side > ball_pos[j].y > -side):
           ball_p[j].y = -ball_p[j].y
        if not (side > ball_pos[j].z > -side):
           ball_p[j].z = -ball_p[j].z
        #print("dupa")
        #print(ball_pos[j].x)
        #print(ball_pos[j][0])
    
    m=0
    #print(balls[99].radius)


    for index, k in enumerate(ball_pos, 1):
        m=m+1

        for l in ball_pos[index:]:
            #print(k)
            #print(round(k.x,2))
            #print(l)
            #print(round(l.x,1)
            
            if ((round(k.x,2)+ball_size-0.2) == (round(l.x,2)+ball_size-0.2)):
                k.x = -k.x
                l.x = -l.x
                #balls[m].color = color.yellow
                #print(balls[m].radius)
                #print(balls[m+1].radius)
                if balls[m-1].radius < 0.3 and balls[m].radius < 0.3:
                    if balls[m-1].radius > balls[m].radius:
                        balls[m-1].radius = balls[m-1].radius + 0.1 #balls.[m].radius
                        balls[m].radius = balls[m].radius - 0.1
                        #balls[m].color = color.yellow
                        #print("dodalo 0.1 do m przy x")
                    else:
                        balls[m].radius = balls[m].radius + 0.1 #balls.[m+1].radius
                        balls[m-1].radius = balls[m-1].radius - 0.1
                        #balls[m].color = color.yellow
                        #print("dodalo 0.1 do m+1 przy x")
            
            elif ((round(k.y,2)+ball_size-0.2) == (round(l.y,2)+ball_size-0.2)):
                k.y = -k.y
                l.y = -l.y
                #balls[m].color = color.yellow
                #balls[m].radius = balls[m].radius +0.1
                if balls[m-1].radius < 0.3 and balls[m].radius < 0.3:
                    if balls[m-1].radius > balls[m].radius:
                        balls[m-1].radius = balls[m-1].radius + 0.01 #balls.[m+1].radius
                        balls[m].radius = balls[m].radius - 0.1
                        #balls[m-1].color = color.yellow
                        #balls[m].visible = False
                        #del balls[m]
                        
                        #print("dodalo 0.1 do m przy y")
                    else:
                        balls[m].radius = balls[m].radius + 0.1 #balls.[m].radius
                        balls[m-1].radius = balls[m-1].radius - 0.1
                        #balls[m].color = color.yellow
                        #print("dodalo 0.1 do m+1 przy y")
            
            elif ((round(k.z,2)+ball_size-0.2) == (round(l.z,2)+ball_size-0.2)):
                k.z = -k.z
                l.z = -l.z
                #balls[m].color = color.yellow
                #balls[m].radius = balls[m].radius +0.1
                if balls[m-1].radius < 0.3 and balls[m].radius < 0.3:
                    if balls[m-1].radius > balls[m].radius:
                        balls[m-1].radius = balls[m-1].radius + 0.1 #balls.[m+1].radius
                        balls[m].radius = balls[m].radius - 0.1
                        #balls[m-1].color = color.yellow
                        #print("dodalo 0.1 do m przy z")
                    else:
                        balls[m].radius = balls[m].radius + 0.1 #balls.[m+1].radius
                        balls[m-1].radius = balls[m-1].radius - 0.1
                        #balls[m].color = color.yellow
                        #print("dodalo 0.1 do m+1 przy z")

        
        

        


        
        

 


        
