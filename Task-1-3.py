from robot import *

for i in range(4):
    paint()
    for j in range(2):
        if(i % 2 == 1):
            move_up()
        else:
            move_down()
    paint()
    move_right()