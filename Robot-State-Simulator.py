import random
import time
robot_state = "MOVING"
previous_state = robot_state
battery = 100
charging = False

while True:
    distance = random.randint(1, 100)
    previous_state = robot_state
    if battery <= 10:
        charging = True
    if charging:
        robot_state = "Recharging Battery"
        print(f"{robot_state}. The battery is {battery}%")
        battery += random.randint(1, 3)
        if battery >= 100:
            battery = 100
            charging = False

    else:
        if distance <= 15:
            robot_state = "STOPPED"

        elif 16 <= distance <= 60:
            robot_state = "SLOWING"
        else:
            robot_state = "MOVING"
        if robot_state != previous_state:
            print(f"{robot_state}. The distance is {distance}. Robot battery is {battery}%")
        battery -= random.randint(1, 5)
    time.sleep(1)