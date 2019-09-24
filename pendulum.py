from visual import *
from numpy import *
from math import *
scene = display(width = 700, height=700, background=[1,1,1], autoscale=1)
gravity = vector(0,-9.8,0)



#table_lines = [1,3,5,7,9,11,13,15,17,19,21]
#linka_przyklad = cylinder (pos = [0,table_lines[0],0], axis=[0,-table_lines[0],0], radius=0.05, color=color.red, table_lines[0]=table_lines[0])


velocity_0 = vector(5,0,0)
dlugosc_l_0 = 4
linka_0 = cylinder (pos=[0,8,8], axis=[0,-dlugosc_l_0,0], radius=0.05, color=color.white, dlugosc_l_0=4)
ciezarek_0 = sphere (radius=1, color=color.red, pos=[0, linka_0.y - dlugosc_l_0, 0])

velocity_01 = vector(5,0,0)
dlugosc_l_01 = 5
linka_01 = cylinder (pos=[0,8,6], axis=[0,-dlugosc_l_01,0], radius=0.05, color=color.white, dlugosc_l_01=5)
ciezarek_01 = sphere (radius=1, color=color.blue, pos=[0, linka_01.y - dlugosc_l_01, 0])


velocity_1 = vector(5,0,0)
dlugosc_l_1 = 6
linka_1 = cylinder (pos=[0,8,4], axis=[0,-dlugosc_l_1,0], radius=0.05, color=color.white, dlugosc_l_1=6)
ciezarek_1 = sphere (radius=1, color=color.red, pos=[0, linka_1.y - dlugosc_l_1, 0])


velocity1 = vector(5,0,0)
dlugosc_l1 = 7
linka1 = cylinder (pos=[0,8,2], axis=[0,-dlugosc_l1,0], radius=0.05, color=color.white, dlugosc_l1=7)
ciezarek1 = sphere(radius=1, color=color.blue, pos=[0,linka1.y - dlugosc_l1,0])


#-------
velocity = vector(5,0,0)
dlugosc_l = 8
linka = cylinder (pos=[0,8,0], axis=[0,-dlugosc_l,0], radius=0.05, color=color.white, dlugosc_l=8)
ciezarek = sphere(radius=1, color=color.red, pos=[0,linka.y - dlugosc_l,0])
#-------

velocity_20 = vector(5,0,0)
dlugosc_l_20 = 9
linka_20 = cylinder (pos=[0,8,-2], axis=[0, -dlugosc_l_20, 0], radius=0.05, color=color.white, dlugosc_l=9)
ciezarek_20 = sphere(radius=1, color=color.blue, pos=[0, linka_20.y - dlugosc_l_20, 0])


velocity_2 = vector(5,0,0)
dlugosc_l_2 = 10
linka_2 = cylinder (pos=[0,8,-4], axis=[0, -dlugosc_l_2, 0], radius=0.05, color=color.white, dlugosc_l=10)
ciezarek_2 = sphere(radius=1, color=color.red, pos=[0, linka_2.y - dlugosc_l_2, 0])


velocity_21 = vector(5,0,0)
dlugosc_l_21 = 11
linka_21 = cylinder (pos=[0,8,-6], axis=[0, -dlugosc_l_21, 0], radius=0.05, color=color.white, dlugosc_l=11)
ciezarek_21 = sphere(radius=1, color=color.blue, pos=[0, linka_21.y - dlugosc_l_21, 0])


velocity_3 = vector(5,0,0)
dlugosc_l_3 = 12
linka_3 = cylinder (pos=[0,8,-8], axis=[0, -dlugosc_l_3, 0], radius=0.05, color=color.white, dlugosc_l_3=12)
ciezarek_3 = sphere(radius=1, color=color.red, pos=[0, linka_3.y - dlugosc_l_3, 0])


velocity_31 = vector(5,0,0)
dlugosc_l_31 = 13
linka_31 = cylinder (pos=[0,8,-10], axis=[0, -dlugosc_l_31, 0], radius=0.05, color=color.white, dlugosc_l_3=13)
ciezarek_31 = sphere(radius=1, color=color.blue, pos=[0, linka_31.y - dlugosc_l_31, 0])

velocity_4 = vector(5,0,0)
dlugosc_l_4 = 14
linka_4 = cylinder (pos=[0,8,-12], axis=[0, -dlugosc_l_4, 0], radius=0.05, color=color.white, dlugosc_l_4=14)
ciezarek_4 = sphere(radius=1, color=color.red, pos=[0, linka_4.y - dlugosc_l_4, 0])

velocity_41 = vector(5,0,0)
dlugosc_l_41 = 15
linka_41 = cylinder (pos=[0,8,-14], axis=[0, -dlugosc_l_41, 0], radius=0.05, color=color.white, dlugosc_l_4=15)
ciezarek_41 = sphere(radius=1, color=color.blue, pos=[0, linka_41.y - dlugosc_l_41, 0])


velocity_5 = vector(5,0,0)
dlugosc_l_5 = 16
linka_5 = cylinder (pos=[0,8,-16], axis=[0, -dlugosc_l_5, 0], radius=0.05, color=color.white, dlugosc_l_5=16)
ciezarek_5 = sphere(radius=1, color=color.red, pos=[0, linka_5.y - dlugosc_l_5, 0])

velocity_51 = vector(5,0,0)
dlugosc_l_51 = 17
linka_51 = cylinder (pos=[0,8,-18], axis=[0, -dlugosc_l_51, 0], radius=0.05, color=color.white, dlugosc_l_51=18)
ciezarek_51 = sphere(radius=1, color=color.blue, pos=[0, linka_51.y - dlugosc_l_51, 0])


velocity_6 = vector(5,0,0)
dlugosc_l_6 = 18
linka_6 = cylinder (pos=[0,8,-20], axis=[0, -dlugosc_l_6, 0], radius=0.05, color=color.white, dlugosc_l_6=18)
ciezarek_6 = sphere(radius=1, color=color.red, pos=[0, linka_6.y - dlugosc_l_6, 0])

velocity_61 = vector(5,0,0)
dlugosc_l_61 = 19
linka_61 = cylinder (pos=[0,8,-22], axis=[0, -dlugosc_l_61, 0], radius=0.05, color=color.white, dlugosc_l_61=19)
ciezarek_61 = sphere(radius=1, color=color.blue, pos=[0, linka_61.y - dlugosc_l_61, 0])


velocity_7 = vector(5,0,0)
dlugosc_l_7 = 20
linka_7 = cylinder (pos=[0,8,-24], axis=[0, -dlugosc_l_7, 0], radius=0.05, color=color.white, dlugosc_l_7=20)
ciezarek_7 = sphere(radius=1, color=color.red, pos=[0, linka_7.y - dlugosc_l_7, 0])


sufit = box(size=[10,0.1,100], color=color.black, pos=[0, 8.1, 0])
dt = 0.09


for i in range(100000):
    sleep(0.02)


    velocity_0.x = velocity_0.x + ciezarek_0.pos.x / dlugosc_l_0 * gravity.y * dt
    ciezarek_0.pos.x = ciezarek_0.pos.x + velocity_0.x*dt
    ciezarek_0.pos.y = dlugosc_l_0 * (1-sqrt(1-(ciezarek_0.pos.x/dlugosc_l_0)**2))
    x = ciezarek_0.pos.x
    y = ciezarek_0.pos.y
    ciezarek_0.pos = [x, y+4, 8]
    linka_0.axis = [x, y - dlugosc_l_0, 0]


    velocity_01.x = velocity_01.x + ciezarek_01.pos.x / dlugosc_l_01 * gravity.y * dt
    ciezarek_01.pos.x = ciezarek_01.pos.x + velocity_01.x*dt
    ciezarek_01.pos.y = dlugosc_l_01 * (1-sqrt(1-(ciezarek_01.pos.x/dlugosc_l_01)**2))
    x = ciezarek_01.pos.x
    y = ciezarek_01.pos.y
    ciezarek_01.pos = [x, y+3, 6]
    linka_01.axis = [x, y - dlugosc_l_01, 0]

    velocity_1.x = velocity_1.x + ciezarek_1.pos.x / dlugosc_l_1 * gravity.y * dt
    ciezarek_1.pos.x = ciezarek_1.pos.x + velocity_1.x*dt
    ciezarek_1.pos.y = dlugosc_l_1 * (1-sqrt(1-(ciezarek_1.pos.x/dlugosc_l_1)**2))
    x = ciezarek_1.pos.x
    y = ciezarek_1.pos.y
    ciezarek_1.pos = [x, y+2, 4]
    linka_1.axis = [x, y - dlugosc_l_1, 0]

    velocity1.x = velocity1.x + ciezarek1.pos.x/dlugosc_l1 * gravity.y * dt
    ciezarek1.pos.x = ciezarek1.pos.x + velocity1.x*dt
    ciezarek1.pos.y = dlugosc_l1 * (1-sqrt(1-(ciezarek1.pos.x/dlugosc_l1)**2))
    x = ciezarek1.pos.x
    y = ciezarek1.pos.y
    ciezarek1.pos = [x, y+1, 2]
    linka1.axis = [x, y-dlugosc_l1, 0]

    #-------------
      
    velocity.x = velocity.x + ciezarek.pos.x/dlugosc_l * gravity.y * dt
    ciezarek.pos.x = ciezarek.pos.x + velocity.x*dt
    ciezarek.pos.y = dlugosc_l * (1-sqrt(1-(ciezarek.pos.x/dlugosc_l)**2))
    x = ciezarek.pos.x
    y = ciezarek.pos.y
    ciezarek.pos = [x, y, 0]
    linka.axis = [x, y-dlugosc_l, 0]

    #------------

    velocity_20.x = velocity_20.x + ciezarek_20.pos.x/dlugosc_l_20 * gravity.y*dt
    ciezarek_20.pos.x = ciezarek_20.pos.x + velocity_20.x * dt
    ciezarek_20.pos.y = dlugosc_l_20 * (1-sqrt(1-(ciezarek_20.pos.x / dlugosc_l_20)**2))
    x = ciezarek_20.pos.x
    y = ciezarek_20.pos.y
    ciezarek_20.pos = [x, y-1, -2]
    linka_20.axis = [x, y - dlugosc_l_20, 0]
    #-------------------------------------------------------
    velocity_2.x = velocity_2.x + ciezarek_2.pos.x/dlugosc_l_2 * gravity.y*dt
    ciezarek_2.pos.x = ciezarek_2.pos.x + velocity_2.x * dt
    ciezarek_2.pos.y = dlugosc_l_2 * (1-sqrt(1-(ciezarek_2.pos.x / dlugosc_l_2)**2))
    x = ciezarek_2.pos.x
    y = ciezarek_2.pos.y
    ciezarek_2.pos = [x, y-2, -4]
    linka_2.axis = [x, y - dlugosc_l_2, 0]


    velocity_21.x = velocity_21.x + ciezarek_21.pos.x/dlugosc_l_21 * gravity.y*dt
    ciezarek_21.pos.x = ciezarek_21.pos.x + velocity_21.x * dt
    ciezarek_21.pos.y = dlugosc_l_21 * (1-sqrt(1-(ciezarek_21.pos.x / dlugosc_l_21)**2))
    x = ciezarek_21.pos.x
    y = ciezarek_21.pos.y
    ciezarek_21.pos = [x, y-3, -6]
    linka_21.axis = [x, y - dlugosc_l_21, 0]

    velocity_3.x = velocity_3.x + ciezarek_3.pos.x/dlugosc_l_3 * gravity.y*dt
    ciezarek_3.pos.x = ciezarek_3.pos.x + velocity_3.x * dt
    ciezarek_3.pos.y = dlugosc_l_3 * (1-sqrt(1-(ciezarek_3.pos.x / dlugosc_l_3)**2))
    x = ciezarek_3.pos.x
    y = ciezarek_3.pos.y
    ciezarek_3.pos = [x, y-4, -8]
    linka_3.axis = [x, y - dlugosc_l_3, 0]


    velocity_31.x = velocity_31.x + ciezarek_31.pos.x/dlugosc_l_31 * gravity.y*dt
    ciezarek_31.pos.x = ciezarek_31.pos.x + velocity_31.x * dt
    ciezarek_31.pos.y = dlugosc_l_31 * (1-sqrt(1-(ciezarek_31.pos.x / dlugosc_l_31)**2))
    x = ciezarek_31.pos.x
    y = ciezarek_31.pos.y
    ciezarek_31.pos = [x, y-5, -10]
    linka_31.axis = [x, y - dlugosc_l_31, 0]


    velocity_4.x = velocity_4.x + ciezarek_4.pos.x/dlugosc_l_4 * gravity.y*dt
    ciezarek_4.pos.x = ciezarek_4.pos.x + velocity_4.x * dt
    ciezarek_4.pos.y = dlugosc_l_4 * (1-sqrt(1-(ciezarek_4.pos.x / dlugosc_l_4)**2))
    x = ciezarek_4.pos.x
    y = ciezarek_4.pos.y
    ciezarek_4.pos = [x, y-6, -12]
    linka_4.axis = [x, y - dlugosc_l_4, 0]


    velocity_41.x = velocity_41.x + ciezarek_41.pos.x/dlugosc_l_41 * gravity.y*dt
    ciezarek_41.pos.x = ciezarek_41.pos.x + velocity_41.x * dt
    ciezarek_41.pos.y = dlugosc_l_41 * (1-sqrt(1-(ciezarek_41.pos.x / dlugosc_l_41)**2))
    x = ciezarek_41.pos.x
    y = ciezarek_41.pos.y
    ciezarek_41.pos = [x, y-7, -14]
    linka_41.axis = [x, y - dlugosc_l_41, 0]


    velocity_5.x = velocity_5.x + ciezarek_5.pos.x/dlugosc_l_5 * gravity.y*dt
    ciezarek_5.pos.x = ciezarek_5.pos.x + velocity_5.x * dt
    ciezarek_5.pos.y = dlugosc_l_5 * (1-sqrt(1-(ciezarek_5.pos.x / dlugosc_l_5)**2))
    x = ciezarek_5.pos.x
    y = ciezarek_5.pos.y
    ciezarek_5.pos = [x, y-8, -16]
    linka_5.axis = [x, y - dlugosc_l_5, 0]

    velocity_51.x = velocity_51.x + ciezarek_51.pos.x/dlugosc_l_51 * gravity.y*dt
    ciezarek_51.pos.x = ciezarek_51.pos.x + velocity_51.x * dt
    ciezarek_51.pos.y = dlugosc_l_51 * (1-sqrt(1-(ciezarek_51.pos.x / dlugosc_l_51)**2))
    x = ciezarek_51.pos.x
    y = ciezarek_51.pos.y
    ciezarek_51.pos = [x, y-9, -18]
    linka_51.axis = [x, y - dlugosc_l_51, 0]


    velocity_6.x = velocity_6.x + ciezarek_6.pos.x/dlugosc_l_6 * gravity.y*dt
    ciezarek_6.pos.x = ciezarek_6.pos.x + velocity_6.x * dt
    ciezarek_6.pos.y = dlugosc_l_6 * (1-sqrt(1-(ciezarek_6.pos.x / dlugosc_l_6)**2))
    x = ciezarek_6.pos.x
    y = ciezarek_6.pos.y
    ciezarek_6.pos = [x, y-10, -20]
    linka_6.axis = [x, y - dlugosc_l_6, 0]


    velocity_61.x = velocity_61.x + ciezarek_61.pos.x/dlugosc_l_61 * gravity.y*dt
    ciezarek_61.pos.x = ciezarek_61.pos.x + velocity_61.x * dt
    ciezarek_61.pos.y = dlugosc_l_61 * (1-sqrt(1-(ciezarek_61.pos.x / dlugosc_l_61)**2))
    x = ciezarek_61.pos.x
    y = ciezarek_61.pos.y
    ciezarek_61.pos = [x, y-11, -22]
    linka_61.axis = [x, y - dlugosc_l_61, 0]
    

    velocity_7.x = velocity_7.x + ciezarek_7.pos.x/dlugosc_l_7 * gravity.y*dt
    ciezarek_7.pos.x = ciezarek_7.pos.x + velocity_7.x * dt
    ciezarek_7.pos.y = dlugosc_l_7 * (1-sqrt(1-(ciezarek_7.pos.x / dlugosc_l_7)**2))
    x = ciezarek_7.pos.x
    y = ciezarek_7.pos.y
    ciezarek_7.pos = [x, y-12, -24]
    linka_7.axis = [x, y - dlugosc_l_7, 0]
